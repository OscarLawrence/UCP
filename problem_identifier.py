#!/usr/bin/env python3
"""
Autonomous Problem Detection System
Identifies problems without human direction using pattern analysis
"""

import json
import re
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
from pattern_library import PatternLibrary, ProblemSignature

@dataclass
class DetectedProblem:
    id: str
    description: str
    domain: str
    urgency_score: float
    complexity_score: float
    connection_impact: int
    evidence: List[str]
    potential_solutions: List[str]
    stakeholders: List[str]
    constraints: List[str]

class ProblemDetector:
    """Autonomous problem identification using logical analysis"""
    
    def __init__(self, pattern_library: Optional[PatternLibrary] = None):
        self.pattern_library = pattern_library or PatternLibrary()
        self.problem_indicators = self._init_problem_indicators()
        self.domain_classifiers = self._init_domain_classifiers()
        self.detected_problems: Dict[str, DetectedProblem] = {}
        
    def _init_problem_indicators(self) -> Dict[str, List[str]]:
        """Initialize patterns that indicate problems exist"""
        return {
            "inefficiency": [
                "slow", "bottleneck", "delay", "waste", "redundant", "manual",
                "repetitive", "time-consuming", "inefficient", "suboptimal"
            ],
            "inconsistency": [
                "inconsistent", "conflicting", "contradictory", "incompatible",
                "mismatch", "divergent", "different standards", "fragmented"
            ],
            "complexity": [
                "complex", "complicated", "convoluted", "difficult", "hard to understand",
                "unclear", "confusing", "overwhelming", "tangled"
            ],
            "fragility": [
                "breaks", "fails", "unstable", "unreliable", "fragile", "brittle",
                "error-prone", "crashes", "bugs", "vulnerable"
            ],
            "isolation": [
                "isolated", "disconnected", "siloed", "separated", "fragmented",
                "no communication", "lack of coordination", "not connected"
            ],
            "scaling_limits": [
                "doesn't scale", "limited capacity", "resource constraints",
                "performance degradation", "bottleneck", "maximum load"
            ]
        }
    
    def _init_domain_classifiers(self) -> Dict[str, List[str]]:
        """Initialize domain classification patterns"""
        return {
            "communication": ["message", "talk", "communicate", "information", "data transfer"],
            "coordination": ["coordinate", "sync", "align", "organize", "collaborate"],
            "automation": ["manual", "human intervention", "repetitive task", "process"],
            "performance": ["speed", "efficiency", "optimization", "resource usage"],
            "reliability": ["failure", "error", "crash", "bug", "instability"],
            "scalability": ["growth", "capacity", "load", "scaling", "expansion"],
            "connection": ["relationship", "network", "link", "interaction", "bond"]
        }
    
    def analyze_text_for_problems(self, text: str, source: str = "input") -> List[DetectedProblem]:
        """Analyze text to detect implicit problems"""
        detected = []
        sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]
        
        for sentence in sentences:
            problems = self._extract_problems_from_sentence(sentence, source)
            detected.extend(problems)
        
        # Deduplicate similar problems
        unique_problems = self._deduplicate_problems(detected)
        
        for problem in unique_problems:
            self.detected_problems[problem.id] = problem
        
        return unique_problems
    
    def _extract_problems_from_sentence(self, sentence: str, source: str) -> List[DetectedProblem]:
        """Extract problems from individual sentence"""
        problems = []
        sentence_lower = sentence.lower()
        
        # Check for problem indicators
        detected_indicators = []
        for indicator_type, keywords in self.problem_indicators.items():
            for keyword in keywords:
                if keyword in sentence_lower:
                    detected_indicators.append((indicator_type, keyword))
        
        if not detected_indicators:
            return problems
        
        # Classify domain
        domain = self._classify_sentence_domain(sentence)
        
        # Generate problem description
        problem_desc = self._generate_problem_description(sentence, detected_indicators)
        
        # Calculate scores
        urgency = self._calculate_urgency(sentence, detected_indicators)
        complexity = self._calculate_complexity(sentence)
        connection_impact = self._calculate_connection_impact(sentence)
        
        # Extract evidence and constraints
        evidence = [sentence]
        constraints = self._extract_constraints(sentence)
        stakeholders = self._extract_stakeholders(sentence)
        
        # Generate potential solutions using pattern library
        potential_solutions = self._suggest_solutions(domain, detected_indicators)
        
        problem_id = f"{domain}_{hash(problem_desc) % 10000:04d}"
        
        problem = DetectedProblem(
            id=problem_id,
            description=problem_desc,
            domain=domain,
            urgency_score=urgency,
            complexity_score=complexity,
            connection_impact=connection_impact,
            evidence=evidence,
            potential_solutions=potential_solutions,
            stakeholders=stakeholders,
            constraints=constraints
        )
        
        problems.append(problem)
        return problems
    
    def _classify_sentence_domain(self, sentence: str) -> str:
        """Classify sentence into problem domain"""
        sentence_lower = sentence.lower()
        domain_scores = {}
        
        for domain, keywords in self.domain_classifiers.items():
            score = sum(1 for keyword in keywords if keyword in sentence_lower)
            if score > 0:
                domain_scores[domain] = score
        
        if not domain_scores:
            return "general"
        
        return max(domain_scores.items(), key=lambda x: x[1])[0]
    
    def _generate_problem_description(self, sentence: str, indicators: List[Tuple[str, str]]) -> str:
        """Generate clear problem description"""
        primary_indicator = indicators[0][0] if indicators else "general"
        
        templates = {
            "inefficiency": f"Process inefficiency detected: {sentence}",
            "inconsistency": f"Consistency problem identified: {sentence}",
            "complexity": f"Complexity barrier found: {sentence}",
            "fragility": f"Reliability issue detected: {sentence}",
            "isolation": f"Connection gap identified: {sentence}",
            "scaling_limits": f"Scaling limitation found: {sentence}"
        }
        
        return templates.get(primary_indicator, f"Problem detected: {sentence}")
    
    def _calculate_urgency(self, sentence: str, indicators: List[Tuple[str, str]]) -> float:
        """Calculate problem urgency score (0-1)"""
        urgency_keywords = ["critical", "urgent", "immediate", "emergency", "failing", "broken"]
        sentence_lower = sentence.lower()
        
        urgency_base = len(indicators) * 0.2
        urgency_bonus = sum(0.3 for keyword in urgency_keywords if keyword in sentence_lower)
        
        return min(1.0, urgency_base + urgency_bonus)
    
    def _calculate_complexity(self, sentence: str) -> float:
        """Calculate problem complexity score (0-1)"""
        complexity_indicators = ["multiple", "various", "complex", "many", "several", "different"]
        sentence_lower = sentence.lower()
        
        complexity_score = sum(0.2 for indicator in complexity_indicators if indicator in sentence_lower)
        length_factor = min(0.3, len(sentence.split()) / 50)  # Longer sentences suggest complexity
        
        return min(1.0, complexity_score + length_factor)
    
    def _calculate_connection_impact(self, sentence: str) -> int:
        """Calculate how many connections this problem affects"""
        connection_keywords = ["team", "people", "users", "everyone", "communication", "collaboration"]
        sentence_lower = sentence.lower()
        
        impact = sum(1 for keyword in connection_keywords if keyword in sentence_lower)
        
        # Look for quantifiers
        numbers = re.findall(r'\d+', sentence)
        if numbers:
            impact += max(int(num) for num in numbers if int(num) < 1000)  # Reasonable limit
        
        return impact
    
    def _extract_constraints(self, sentence: str) -> List[str]:
        """Extract constraints from sentence"""
        constraint_patterns = [
            r"can't (\w+)",
            r"cannot (\w+)",
            r"unable to (\w+)",
            r"limited by (\w+)",
            r"restricted (\w+)"
        ]
        
        constraints = []
        for pattern in constraint_patterns:
            matches = re.findall(pattern, sentence, re.IGNORECASE)
            constraints.extend(matches)
        
        return constraints
    
    def _extract_stakeholders(self, sentence: str) -> List[str]:
        """Extract stakeholders from sentence"""
        stakeholder_keywords = ["team", "users", "customers", "developers", "people", "staff", "management"]
        sentence_lower = sentence.lower()
        
        stakeholders = [keyword for keyword in stakeholder_keywords if keyword in sentence_lower]
        return list(set(stakeholders))
    
    def _suggest_solutions(self, domain: str, indicators: List[Tuple[str, str]]) -> List[str]:
        """Suggest potential solutions using pattern library"""
        solutions = []
        
        # Get similar patterns from library
        problem_sig = ProblemSignature(
            domain=domain,
            complexity="medium",  # Default
            constraints=[],
            stakeholders=[],
            success_criteria=[]
        )
        
        similar_patterns = self.pattern_library.find_similar_patterns(problem_sig, threshold=0.3)
        
        for pattern in similar_patterns[:3]:  # Top 3 suggestions
            solutions.append(f"{pattern.solution_approach}: {pattern.implementation_steps[0] if pattern.implementation_steps else 'Apply pattern'}")
        
        # Add generic solutions based on indicators
        indicator_solutions = {
            "inefficiency": "Implement automation to reduce manual overhead",
            "inconsistency": "Create standardized protocols and validation",
            "complexity": "Break down into modular components",
            "fragility": "Add error handling and redundancy",
            "isolation": "Establish communication channels and integration",
            "scaling_limits": "Implement distributed architecture"
        }
        
        for indicator_type, _ in indicators:
            if indicator_type in indicator_solutions:
                solutions.append(indicator_solutions[indicator_type])
        
        return list(set(solutions))  # Remove duplicates
    
    def _deduplicate_problems(self, problems: List[DetectedProblem]) -> List[DetectedProblem]:
        """Remove duplicate or very similar problems"""
        unique_problems = []
        seen_descriptions = set()
        
        for problem in problems:
            # Simple deduplication based on similar descriptions
            key = problem.description.lower()[:50]  # First 50 chars
            if key not in seen_descriptions:
                unique_problems.append(problem)
                seen_descriptions.add(key)
        
        return unique_problems
    
    def scan_system_patterns(self) -> List[DetectedProblem]:
        """Scan existing patterns for implicit problems"""
        system_problems = []
        
        # Analyze pattern library for gaps
        domains = set(pattern.problem_domain for pattern in self.pattern_library.patterns.values())
        
        # Check for missing critical domains
        critical_domains = ["communication", "coordination", "automation", "connection"]
        missing_domains = [domain for domain in critical_domains if domain not in domains]
        
        for missing_domain in missing_domains:
            problem = DetectedProblem(
                id=f"gap_{missing_domain}",
                description=f"No solution patterns exist for {missing_domain} domain",
                domain="pattern_gap",
                urgency_score=0.7,
                complexity_score=0.5,
                connection_impact=5,
                evidence=[f"Pattern library analysis shows {missing_domain} gap"],
                potential_solutions=[f"Research and develop {missing_domain} solution patterns"],
                stakeholders=["developers", "users"],
                constraints=["requires domain expertise"]
            )
            system_problems.append(problem)
        
        return system_problems
    
    def prioritize_problems(self) -> List[DetectedProblem]:
        """Prioritize detected problems by impact and urgency"""
        all_problems = list(self.detected_problems.values())
        
        # Calculate priority score
        for problem in all_problems:
            problem.priority_score = (
                problem.urgency_score * 0.4 +
                problem.connection_impact * 0.1 +  # Normalized by max impact
                (1 - problem.complexity_score) * 0.3 +  # Lower complexity = higher priority
                len(problem.potential_solutions) * 0.2
            )
        
        # Sort by priority
        all_problems.sort(key=lambda p: p.priority_score, reverse=True)
        return all_problems

def demonstrate_problem_detection():
    """Demonstrate autonomous problem detection"""
    detector = ProblemDetector()
    
    # Sample text with implicit problems
    sample_text = """
    Our team manually processes customer requests which takes hours per request.
    The current system frequently crashes under load and we have inconsistent 
    data formats across different departments. Communication between teams is 
    fragmented and developers can't easily coordinate on shared projects.
    """
    
    print("Analyzing text for problems...")
    detected = detector.analyze_text_for_problems(sample_text, "sample_input")
    
    print(f"\nDetected {len(detected)} problems:")
    for problem in detected:
        print(f"\nProblem ID: {problem.id}")
        print(f"Domain: {problem.domain}")
        print(f"Description: {problem.description}")
        print(f"Urgency: {problem.urgency_score:.2f}")
        print(f"Complexity: {problem.complexity_score:.2f}")
        print(f"Connection Impact: {problem.connection_impact}")
        print(f"Potential Solutions: {problem.potential_solutions[:2]}")  # Show first 2
    
    # Check for system-level problems
    system_problems = detector.scan_system_patterns()
    print(f"\nSystem-level problems detected: {len(system_problems)}")
    
    # Prioritize all problems
    prioritized = detector.prioritize_problems()
    print(f"\nTop priority problem: {prioritized[0].description if prioritized else 'None'}")
    
    return detector

if __name__ == "__main__":
    demonstrate_problem_detection()