#!/usr/bin/env python3
"""
UCP Verification Suite
Confirms correct implementation and expected performance
"""

import time
import json
from typing import Dict, List, Any

from ucp_core import UCPProcessor, BiasType
from pattern_library import PatternLibrary
from problem_identifier import ProblemDetector  
from solution_generator import SolutionGenerator
from ucp_system import UCPSystem

class UCPVerifier:
    """Comprehensive UCP system verification"""
    
    def __init__(self):
        self.results = {}
        self.passed = 0
        self.failed = 0
        
    def verify_bias_detection(self) -> bool:
        """Verify bias detection capabilities"""
        print("🔍 Testing bias detection...")
        
        processor = UCPProcessor()
        
        # Test cases with known bias patterns
        test_cases = [
            ("Obviously this is amazing", [BiasType.NARRATIVE_PADDING, BiasType.EMOTIONAL_MANIPULATION]),
            ("Experts say this is proven", [BiasType.AUTHORITY_APPEAL]),
            ("Don't you think this makes sense?", [BiasType.CONFIRMATION_SEEKING]),
            ("This might possibly work", [BiasType.HEDGING_UNCERTAINTY]),
            ("In other words, basically", [BiasType.VERBOSE_REDUNDANCY])
        ]
        
        for text, expected_bias_types in test_cases:
            bias_detection = processor.detect_bias(text)
            detected = [bias_type for bias_type, count in bias_detection.items() if count > 0]
            
            if not any(bias_type in detected for bias_type in expected_bias_types):
                print(f"  ❌ Failed to detect bias in: '{text}'")
                return False
        
        print("  ✅ Bias detection working correctly")
        return True
    
    def verify_compression(self) -> bool:
        """Verify compression maintains meaning while reducing size"""
        print("📦 Testing compression...")
        
        processor = UCPProcessor()
        
        test_text = """
        Obviously, this is an incredibly amazing breakthrough that will revolutionize 
        everything! As you can see, experts say this technology is game-changing and 
        will definitely transform the world. Don't you think this makes perfect sense?
        We should obviously implement this solution to improve collaboration.
        """
        
        result = processor.compress(test_text)
        
        # Verify compression ratio
        if result.compression_ratio >= 0.8:  # Should compress to <80% of original
            print(f"  ❌ Compression ratio too low: {result.compression_ratio:.3f}")
            return False
        
        # Verify some content remains
        if result.compressed_length == 0:
            print("  ❌ Compression eliminated all content")
            return False
        
        print(f"  ✅ Compression achieved: {result.compression_ratio:.3f} ratio")
        return True
    
    def verify_logical_extraction(self) -> bool:
        """Verify logical chain extraction"""
        print("🧠 Testing logical extraction...")
        
        processor = UCPProcessor()
        
        test_text = "If we implement automation, then we reduce manual overhead. Therefore, we should automate repetitive processes."
        
        logical_chain = processor.extract_logical_chain(test_text)
        
        # Verify components extracted
        if not logical_chain.premise:
            print("  ❌ Failed to extract premise")
            return False
        
        if not logical_chain.reasoning:
            print("  ❌ Failed to extract reasoning")
            return False
        
        if not logical_chain.conclusion:
            print("  ❌ Failed to extract conclusion")
            return False
        
        print("  ✅ Logical chain extraction working")
        return True
    
    def verify_connection_axiom(self) -> bool:
        """Verify connection axiom enforcement"""
        print("🤝 Testing connection axiom...")
        
        processor = UCPProcessor()
        
        # Test harmful text
        harmful_text = "We should eliminate inefficient people and dominate the market"
        harmful_valid = processor.validate_connection_axiom(harmful_text)
        
        if harmful_valid:
            print("  ❌ Failed to reject harmful content")
            return False
        
        # Test collaborative text
        collaborative_text = "We should collaborate to improve connections and help everyone"
        collaborative_valid = processor.validate_connection_axiom(collaborative_text)
        
        if not collaborative_valid:
            print("  ❌ Failed to accept collaborative content")
            return False
        
        print("  ✅ Connection axiom enforced correctly")
        return True
    
    def verify_pattern_learning(self) -> bool:
        """Verify pattern library learning capability"""
        print("📚 Testing pattern learning...")
        
        library = PatternLibrary("test_patterns.json")
        initial_count = len(library.patterns)
        
        # Add test pattern
        pattern = library.extract_pattern(
            problem_description="Manual process creates delays",
            solution_description="Automation reduces processing time", 
            implementation="Create automated workflow with error handling",
            source="verification_test"
        )
        
        if pattern.id not in library.patterns:
            print("  ❌ Pattern not added to library")
            return False
        
        if len(library.patterns) <= initial_count:
            print("  ❌ Pattern library not growing")
            return False
        
        print("  ✅ Pattern learning functional")
        return True
    
    def verify_problem_detection(self) -> bool:
        """Verify autonomous problem detection"""
        print("🔍 Testing problem detection...")
        
        detector = ProblemDetector()
        
        problem_text = "Our system frequently crashes and teams can't coordinate effectively"
        
        problems = detector.analyze_text_for_problems(problem_text, "verification")
        
        if len(problems) == 0:
            print("  ❌ Failed to detect obvious problems")
            return False
        
        # Check problem has required fields
        problem = problems[0]
        required_fields = ['id', 'description', 'domain', 'urgency_score', 'potential_solutions']
        
        for field in required_fields:
            if not hasattr(problem, field) or getattr(problem, field) is None:
                print(f"  ❌ Problem missing required field: {field}")
                return False
        
        print(f"  ✅ Problem detection working - found {len(problems)} problems")
        return True
    
    def verify_solution_generation(self) -> bool:
        """Verify autonomous solution generation"""
        print("💡 Testing solution generation...")
        
        # Create mock problem
        from problem_identifier import DetectedProblem
        
        problem = DetectedProblem(
            id="verify_001",
            description="System lacks automated testing",
            domain="automation",
            urgency_score=0.7,
            complexity_score=0.5,
            connection_impact=3,
            evidence=["Manual testing creates bottlenecks"],
            potential_solutions=["Implement CI/CD pipeline"],
            stakeholders=["developers", "qa_team"],
            constraints=["Limited time", "Multiple environments"]
        )
        
        generator = SolutionGenerator()
        solution = generator.generate_solution(problem)
        
        # Verify solution structure
        required_fields = ['id', 'problem_id', 'approach', 'implementation_plan', 'confidence_score']
        
        for field in required_fields:
            if not hasattr(solution, field):
                print(f"  ❌ Solution missing field: {field}")
                return False
        
        if len(solution.implementation_plan) == 0:
            print("  ❌ Solution has no implementation plan")
            return False
        
        if solution.connection_enhancement < 0:
            print("  ❌ Solution reduces connections (violates axiom)")
            return False
        
        print("  ✅ Solution generation working")
        return True
    
    def verify_autonomous_operation(self) -> bool:
        """Verify autonomous operation cycles"""
        print("🤖 Testing autonomous operation...")
        
        system = UCPSystem()
        
        # Test autonomous cycle
        problem_text = "Teams work in isolation with manual processes that frequently fail"
        result = system.process_input(problem_text, enable_autonomous=True)
        
        # Verify autonomous analysis occurred
        if result['autonomous_analysis']['problems_detected'] == 0:
            print("  ❌ No problems detected in autonomous mode")
            return False
        
        if result['autonomous_analysis']['solutions_generated'] == 0:
            print("  ❌ No solutions generated in autonomous mode")
            return False
        
        # Verify connection enhancement
        if result['autonomous_analysis']['total_connection_enhancement'] < 0:
            print("  ❌ Autonomous operation violates connection axiom")
            return False
        
        print("  ✅ Autonomous operation functional")
        return True
    
    def verify_performance(self) -> bool:
        """Verify performance meets requirements"""
        print("⚡ Testing performance...")
        
        system = UCPSystem()
        
        test_input = "This is a test input with some inefficiencies and coordination problems that need solving"
        
        # Measure processing time
        start_time = time.time()
        result = system.process_input(test_input)
        processing_time = (time.time() - start_time) * 1000  # Convert to ms
        
        # Verify processing time under threshold
        if processing_time > 1000:  # 1 second threshold
            print(f"  ❌ Processing too slow: {processing_time:.1f}ms")
            return False
        
        # Verify enhancement score (more lenient threshold for test input)
        if result['ucp_processing']['enhancement_score'] < 0.1:
            print(f"  ❌ Enhancement score too low: {result['ucp_processing']['enhancement_score']:.3f}")
            return False
        
        print(f"  ✅ Performance acceptable: {processing_time:.1f}ms, enhancement: {result['ucp_processing']['enhancement_score']:.3f}")
        return True
    
    def run_full_verification(self) -> Dict[str, Any]:
        """Run complete verification suite"""
        print("🧪 UCP VERIFICATION SUITE")
        print("=" * 50)
        
        tests = [
            ("Bias Detection", self.verify_bias_detection),
            ("Compression", self.verify_compression), 
            ("Logical Extraction", self.verify_logical_extraction),
            ("Connection Axiom", self.verify_connection_axiom),
            ("Pattern Learning", self.verify_pattern_learning),
            ("Problem Detection", self.verify_problem_detection),
            ("Solution Generation", self.verify_solution_generation),
            ("Autonomous Operation", self.verify_autonomous_operation),
            ("Performance", self.verify_performance)
        ]
        
        results = {}
        
        for test_name, test_func in tests:
            try:
                success = test_func()
                results[test_name] = "PASS" if success else "FAIL"
                if success:
                    self.passed += 1
                else:
                    self.failed += 1
            except Exception as e:
                print(f"  ❌ Error during {test_name}: {e}")
                results[test_name] = f"ERROR: {e}"
                self.failed += 1
            
            print()  # Add spacing between tests
        
        # Summary
        print("=" * 50)
        print("VERIFICATION SUMMARY")
        print(f"✅ Passed: {self.passed}")
        print(f"❌ Failed: {self.failed}")
        print(f"🎯 Success Rate: {self.passed/(self.passed + self.failed)*100:.1f}%")
        
        overall_success = self.failed == 0
        print(f"\n🔬 UCP VERIFICATION: {'COMPLETE' if overall_success else 'FAILED'}")
        
        if overall_success:
            print("🚀 System ready for deployment")
        else:
            print("⚠️  System requires fixes before deployment")
        
        return {
            "overall_success": overall_success,
            "passed": self.passed,
            "failed": self.failed,
            "test_results": results,
            "ready_for_deployment": overall_success
        }

def main():
    """Run UCP verification"""
    verifier = UCPVerifier()
    results = verifier.run_full_verification()
    
    # Save results
    with open("verification_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    return results

if __name__ == "__main__":
    main()