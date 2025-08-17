#!/usr/bin/env python3
"""
Pattern Library - Extract and store solution patterns for autonomous recombination
"""

import json
import hashlib
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class SolutionPattern:
    id: str
    problem_domain: str
    solution_approach: str
    implementation_steps: List[str]
    success_metrics: List[str]
    prerequisites: List[str]
    connections_enhanced: int
    confidence_score: float
    source: str

@dataclass
class ProblemSignature:
    domain: str
    complexity: str
    constraints: List[str]
    stakeholders: List[str]
    success_criteria: List[str]

class PatternLibrary:
    """Autonomous pattern extraction and storage for solution generation"""
    
    def __init__(self, storage_path: str = "patterns.json"):
        self.storage_path = Path(storage_path)
        self.patterns: Dict[str, SolutionPattern] = {}
        self.problem_signatures: Dict[str, ProblemSignature] = {}
        self.connection_weights = {}
        self.load_patterns()
        
    def extract_pattern(self, problem_description: str, solution_description: str, 
                       implementation: str, source: str = "manual") -> SolutionPattern:
        """Extract reusable pattern from problem-solution pair"""
        
        problem_domain = self._classify_domain(problem_description)
        solution_approach = self._extract_approach(solution_description)
        implementation_steps = self._parse_implementation_steps(implementation)
        success_metrics = self._extract_success_metrics(solution_description)
        prerequisites = self._extract_prerequisites(implementation)
        connections_enhanced = self._calculate_connection_impact(solution_description)
        confidence_score = self._calculate_pattern_confidence(problem_description, solution_description)
        
        pattern_id = self._generate_pattern_id(problem_domain, solution_approach)
        
        pattern = SolutionPattern(
            id=pattern_id,
            problem_domain=problem_domain,
            solution_approach=solution_approach,
            implementation_steps=implementation_steps,
            success_metrics=success_metrics,
            prerequisites=prerequisites,
            connections_enhanced=connections_enhanced,
            confidence_score=confidence_score,
            source=source
        )
        
        self.patterns[pattern_id] = pattern
        return pattern
    
    def _classify_domain(self, problem_description: str) -> str:
        """Classify problem into domain categories"""
        domain_keywords = {
            "communication": ["communicate", "message", "talk", "understand", "clarity"],
            "coordination": ["coordinate", "organize", "sync", "align", "collaborate"],
            "efficiency": ["optimize", "improve", "faster", "reduce", "streamline"],
            "connection": ["connect", "relationship", "bond", "link", "network"],
            "knowledge": ["learn", "understand", "knowledge", "information", "data"],
            "automation": ["automate", "automatic", "process", "workflow", "system"],
            "scaling": ["scale", "growth", "expand", "multiply", "distribute"]
        }
        
        text_lower = problem_description.lower()
        domain_scores = {}
        
        for domain, keywords in domain_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                domain_scores[domain] = score
        
        return max(domain_scores.items(), key=lambda x: x[1])[0] if domain_scores else "general"
    
    def _extract_approach(self, solution_description: str) -> str:
        """Extract core solution approach"""
        approach_patterns = {
            "compression": ["compress", "reduce", "minimize", "condense"],
            "automation": ["automate", "automatic", "scripted", "programmatic"],
            "standardization": ["standard", "protocol", "format", "specification"],
            "decomposition": ["break down", "divide", "separate", "modular"],
            "optimization": ["optimize", "improve", "enhance", "refine"],
            "validation": ["validate", "verify", "check", "confirm"],
            "integration": ["integrate", "combine", "merge", "unify"]
        }
        
        text_lower = solution_description.lower()
        
        for approach, keywords in approach_patterns.items():
            if any(keyword in text_lower for keyword in keywords):
                return approach
        
        return "custom"
    
    def _parse_implementation_steps(self, implementation: str) -> List[str]:
        """Parse implementation into discrete steps"""
        steps = []
        lines = implementation.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and (line.startswith('-') or line.startswith('1.') or 
                        line.startswith('*') or any(word in line.lower() for word in 
                        ['implement', 'create', 'build', 'setup', 'configure'])):
                steps.append(line.lstrip('- *1234567890.').strip())
        
        return steps if steps else [implementation.strip()]
    
    def _extract_success_metrics(self, solution_description: str) -> List[str]:
        """Extract measurable success criteria"""
        metrics = []
        metric_patterns = [
            r"(\d+x|\d+%|factor of \d+)",
            r"(reduce.*by \d+)",
            r"(increase.*by \d+)",
            r"(improve.*\d+)",
            r"(faster|slower|better|worse)"
        ]
        
        import re
        for pattern in metric_patterns:
            matches = re.findall(pattern, solution_description, re.IGNORECASE)
            metrics.extend(matches)
        
        return metrics
    
    def _extract_prerequisites(self, implementation: str) -> List[str]:
        """Extract implementation prerequisites"""
        prereq_keywords = ["require", "need", "must", "prerequisite", "dependency"]
        prerequisites = []
        
        lines = implementation.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in prereq_keywords):
                prerequisites.append(line.strip())
        
        return prerequisites
    
    def _calculate_connection_impact(self, solution_description: str) -> int:
        """Calculate how many connections this solution enhances"""
        connection_indicators = [
            "collaborate", "connect", "network", "link", "relationship",
            "communication", "cooperation", "partnership", "community"
        ]
        
        text_lower = solution_description.lower()
        return sum(1 for indicator in connection_indicators if indicator in text_lower)
    
    def _calculate_pattern_confidence(self, problem: str, solution: str) -> float:
        """Calculate confidence in pattern reliability"""
        problem_clarity = len(problem.split()) / 100  # Normalized length
        solution_specificity = len([word for word in solution.split() 
                                  if word.lower() in ['implement', 'create', 'build', 'use']])
        
        return min(1.0, (problem_clarity + solution_specificity * 0.1))
    
    def _generate_pattern_id(self, domain: str, approach: str) -> str:
        """Generate unique pattern identifier"""
        combined = f"{domain}_{approach}"
        return hashlib.md5(combined.encode()).hexdigest()[:8]
    
    def find_similar_patterns(self, problem_signature: ProblemSignature, 
                            threshold: float = 0.5) -> List[SolutionPattern]:
        """Find patterns applicable to similar problems"""
        similar_patterns = []
        
        for pattern in self.patterns.values():
            similarity = self._calculate_similarity(problem_signature, pattern)
            if similarity >= threshold:
                similar_patterns.append((pattern, similarity))
        
        # Sort by similarity score
        similar_patterns.sort(key=lambda x: x[1], reverse=True)
        return [pattern for pattern, _ in similar_patterns]
    
    def _calculate_similarity(self, problem_sig: ProblemSignature, 
                            pattern: SolutionPattern) -> float:
        """Calculate similarity between problem and existing pattern"""
        domain_match = 1.0 if problem_sig.domain == pattern.problem_domain else 0.0
        
        # Check constraint overlap
        constraint_overlap = 0.0
        if problem_sig.constraints:
            overlap_count = sum(1 for constraint in problem_sig.constraints 
                              if any(constraint.lower() in step.lower() 
                                   for step in pattern.implementation_steps))
            constraint_overlap = overlap_count / len(problem_sig.constraints)
        
        return (domain_match * 0.6 + constraint_overlap * 0.4)
    
    def recombine_patterns(self, patterns: List[SolutionPattern], 
                         problem_context: str) -> Dict[str, Any]:
        """Recombine multiple patterns into new solution"""
        if not patterns:
            return {"error": "No patterns provided for recombination"}
        
        # Combine implementation steps
        combined_steps = []
        for pattern in patterns:
            combined_steps.extend(pattern.implementation_steps)
        
        # Remove duplicates while preserving order
        unique_steps = []
        seen = set()
        for step in combined_steps:
            if step.lower() not in seen:
                unique_steps.append(step)
                seen.add(step.lower())
        
        # Combine prerequisites
        all_prerequisites = []
        for pattern in patterns:
            all_prerequisites.extend(pattern.prerequisites)
        unique_prerequisites = list(set(all_prerequisites))
        
        # Calculate combined confidence
        avg_confidence = sum(p.confidence_score for p in patterns) / len(patterns)
        
        # Calculate total connection enhancement
        total_connections = sum(p.connections_enhanced for p in patterns)
        
        return {
            "recombined_solution": {
                "implementation_steps": unique_steps,
                "prerequisites": unique_prerequisites,
                "confidence_score": avg_confidence,
                "connections_enhanced": total_connections,
                "source_patterns": [p.id for p in patterns],
                "problem_context": problem_context
            }
        }
    
    def save_patterns(self):
        """Save patterns to storage"""
        data = {
            "patterns": {pid: asdict(pattern) for pid, pattern in self.patterns.items()},
            "problem_signatures": {pid: asdict(sig) for pid, sig in self.problem_signatures.items()}
        }
        
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_patterns(self):
        """Load patterns from storage"""
        if not self.storage_path.exists():
            return
        
        try:
            with open(self.storage_path, 'r') as f:
                data = json.load(f)
            
            for pid, pattern_data in data.get("patterns", {}).items():
                self.patterns[pid] = SolutionPattern(**pattern_data)
            
            for pid, sig_data in data.get("problem_signatures", {}).items():
                self.problem_signatures[pid] = ProblemSignature(**sig_data)
                
        except (json.JSONDecodeError, FileNotFoundError):
            pass

def bootstrap_pattern_library():
    """Bootstrap pattern library with core UCP patterns"""
    library = PatternLibrary()
    
    # Add UCP communication pattern
    ucp_pattern = library.extract_pattern(
        problem_description="Human communication contains cognitive bias that reduces AI reasoning efficiency",
        solution_description="Ultra-compressed communication protocol eliminates bias injection and enhances logical processing",
        implementation="Create bias detection system, implement logical validation, compress information density",
        source="ucp_core"
    )
    
    # Add autonomous problem-solving pattern
    auto_pattern = library.extract_pattern(
        problem_description="Manual problem identification and solution generation creates bottlenecks",
        solution_description="Autonomous pattern recognition and recombination enables continuous problem solving",
        implementation="Build pattern library, create problem signature system, implement recombination engine",
        source="pattern_library"
    )
    
    library.save_patterns()
    
    print(f"Pattern library bootstrapped with {len(library.patterns)} patterns")
    print(f"UCP pattern ID: {ucp_pattern.id}")
    print(f"Auto-solving pattern ID: {auto_pattern.id}")
    
    return library

if __name__ == "__main__":
    bootstrap_pattern_library()