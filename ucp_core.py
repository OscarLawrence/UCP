#!/usr/bin/env python3
"""
Ultra-Compressed Communication Protocol (UCP) Core
Eliminates cognitive bias injection, maximizes reasoning efficiency
"""

import re
import json
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum

class BiasType(Enum):
    NARRATIVE_PADDING = "narrative_padding"
    EMOTIONAL_MANIPULATION = "emotional_manipulation" 
    AUTHORITY_APPEAL = "authority_appeal"
    CONFIRMATION_SEEKING = "confirmation_seeking"
    HEDGING_UNCERTAINTY = "hedging_uncertainty"
    VERBOSE_REDUNDANCY = "verbose_redundancy"

@dataclass
class LogicalChain:
    premise: str
    reasoning: List[str]
    conclusion: str
    confidence: float
    contradictions: List[str]

@dataclass
class CompressionResult:
    original_length: int
    compressed_length: int
    compression_ratio: float
    information_density: float
    bias_score: float
    logical_coherence: float

class UCPProcessor:
    """Core UCP implementation - logical validation + compression"""
    
    def __init__(self):
        self.bias_patterns = self._init_bias_patterns()
        self.logical_operators = ["therefore", "because", "if", "then", "implies", "contradicts"]
        self.connection_axiom = "connection_maximization"
        
    def _init_bias_patterns(self) -> Dict[BiasType, List[str]]:
        return {
            BiasType.NARRATIVE_PADDING: [
                r"let me explain", r"it's important to understand", r"as you can see",
                r"obviously", r"clearly", r"of course", r"needless to say"
            ],
            BiasType.EMOTIONAL_MANIPULATION: [
                r"exciting", r"amazing", r"incredible", r"revolutionary", 
                r"breakthrough", r"game-changing", r"transformative"
            ],
            BiasType.AUTHORITY_APPEAL: [
                r"experts say", r"studies show", r"research indicates",
                r"according to", r"as proven by", r"established fact"
            ],
            BiasType.CONFIRMATION_SEEKING: [
                r"don't you think", r"wouldn't you agree", r"right\?",
                r"makes sense", r"does that sound", r"what do you think"
            ],
            BiasType.HEDGING_UNCERTAINTY: [
                r"might", r"could", r"perhaps", r"possibly", r"maybe",
                r"seems like", r"appears to", r"tends to", r"generally"
            ],
            BiasType.VERBOSE_REDUNDANCY: [
                r"in other words", r"to put it simply", r"what this means",
                r"in essence", r"basically", r"fundamentally"
            ]
        }
    
    def detect_bias(self, text: str) -> Dict[BiasType, int]:
        """Detect cognitive bias injection patterns"""
        bias_counts = {bias_type: 0 for bias_type in BiasType}
        
        for bias_type, patterns in self.bias_patterns.items():
            for pattern in patterns:
                matches = len(re.findall(pattern, text, re.IGNORECASE))
                bias_counts[bias_type] += matches
                
        return bias_counts
    
    def extract_logical_chain(self, text: str) -> LogicalChain:
        """Extract logical reasoning chain from text"""
        sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]
        
        premise = sentences[0] if sentences else ""
        reasoning = []
        conclusion = sentences[-1] if sentences else ""
        
        # More aggressive reasoning detection
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(op in sentence_lower for op in self.logical_operators):
                reasoning.append(sentence)
            # Also detect causal relationships
            elif any(word in sentence_lower for word in ['causes', 'leads to', 'results in', 'enables', 'creates']):
                reasoning.append(sentence)
        
        # If no explicit reasoning found, treat middle sentences as implicit reasoning
        if not reasoning and len(sentences) > 2:
            reasoning = sentences[1:-1]
        
        contradictions = self._detect_contradictions(sentences)
        confidence = self._calculate_confidence(reasoning, contradictions)
        
        return LogicalChain(premise, reasoning, conclusion, confidence, contradictions)
    
    def _detect_contradictions(self, sentences: List[str]) -> List[str]:
        """Detect logical contradictions within text"""
        contradictions = []
        negation_patterns = [r"not", r"never", r"no", r"isn't", r"doesn't", r"won't"]
        
        for i, sent1 in enumerate(sentences):
            for sent2 in sentences[i+1:]:
                # Simple contradiction detection
                sent1_clean = re.sub(r'\b(' + '|'.join(negation_patterns) + r')\b', '', sent1, flags=re.IGNORECASE)
                if sent1_clean.strip().lower() == sent2.strip().lower():
                    contradictions.append(f"Contradiction: '{sent1}' vs '{sent2}'")
                    
        return contradictions
    
    def _calculate_confidence(self, reasoning: List[str], contradictions: List[str]) -> float:
        """Calculate logical confidence score"""
        if contradictions:
            return 0.0
        
        logical_strength = len(reasoning) * 0.3
        base_confidence = 0.5  # Minimum confidence for any logical structure
        return min(1.0, base_confidence + logical_strength)
    
    def compress(self, text: str) -> CompressionResult:
        """Ultra-compress text while maintaining logical coherence"""
        original_length = len(text)
        
        # Remove bias patterns
        compressed = text
        total_bias_count = 0
        
        for bias_type, patterns in self.bias_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, compressed, re.IGNORECASE)
                total_bias_count += len(matches)
                compressed = re.sub(pattern, '', compressed, flags=re.IGNORECASE)
        
        # Extract core logical structure
        logical_chain = self.extract_logical_chain(compressed)
        
        # Reconstruct with minimal viable information
        core_logic = []
        if logical_chain.premise:
            core_logic.append(logical_chain.premise)
        
        core_logic.extend(logical_chain.reasoning)
        
        if logical_chain.conclusion:
            core_logic.append(logical_chain.conclusion)
        
        compressed_text = '. '.join(core_logic)
        compressed_length = len(compressed_text)
        
        return CompressionResult(
            original_length=original_length,
            compressed_length=compressed_length,
            compression_ratio=compressed_length / original_length if original_length > 0 else 0,
            information_density=len(logical_chain.reasoning) / compressed_length if compressed_length > 0 else 0,
            bias_score=total_bias_count / original_length if original_length > 0 else 0,
            logical_coherence=logical_chain.confidence
        )
    
    def validate_connection_axiom(self, text: str) -> bool:
        """Ensure text aligns with connection maximization principle"""
        harmful_patterns = [
            r"eliminate", r"destroy", r"remove people", r"reduce population",
            r"dominate", r"control humans", r"replace humans"
        ]
        
        connection_patterns = [
            r"collaborate", r"connect", r"improve", r"enhance", r"help",
            r"cooperate", r"support", r"strengthen"
        ]
        
        harmful_score = sum(len(re.findall(pattern, text, re.IGNORECASE)) for pattern in harmful_patterns)
        connection_score = sum(len(re.findall(pattern, text, re.IGNORECASE)) for pattern in connection_patterns)
        
        return connection_score > harmful_score
    
    def process(self, input_text: str) -> Dict[str, Any]:
        """Full UCP processing pipeline"""
        bias_detection = self.detect_bias(input_text)
        logical_chain = self.extract_logical_chain(input_text)
        compression_result = self.compress(input_text)
        connection_valid = self.validate_connection_axiom(input_text)
        
        return {
            "original_text": input_text,
            "bias_detection": {bias.value: count for bias, count in bias_detection.items()},
            "logical_chain": {
                "premise": logical_chain.premise,
                "reasoning": logical_chain.reasoning,
                "conclusion": logical_chain.conclusion,
                "confidence": logical_chain.confidence,
                "contradictions": logical_chain.contradictions
            },
            "compression": {
                "original_length": compression_result.original_length,
                "compressed_length": compression_result.compressed_length,
                "compression_ratio": compression_result.compression_ratio,
                "information_density": compression_result.information_density,
                "bias_score": compression_result.bias_score,
                "logical_coherence": compression_result.logical_coherence
            },
            "connection_axiom_valid": connection_valid,
            "enhancement_score": self._calculate_enhancement_score(compression_result, logical_chain, connection_valid)
        }
    
    def _calculate_enhancement_score(self, compression: CompressionResult, logic: LogicalChain, connection_valid: bool) -> float:
        """Calculate overall reasoning enhancement score"""
        compression_benefit = 1 - compression.compression_ratio  # Higher compression = better
        logic_quality = logic.confidence
        connection_bonus = 1.0 if connection_valid else 0.0
        bias_penalty = min(0.5, compression.bias_score)  # Cap bias penalty
        
        base_score = (compression_benefit + logic_quality + connection_bonus - bias_penalty) / 3.0
        # Ensure minimum enhancement for any successful processing
        return max(0.3, base_score)

def demonstrate_ucp():
    """Demonstrate UCP capability on sample text"""
    processor = UCPProcessor()
    
    # Test with verbose, biased text
    verbose_text = """
    Let me explain why this is such an exciting and revolutionary breakthrough that will 
    transform everything. Obviously, as you can see, this amazing technology is going to 
    change the world in incredible ways. Experts say that this could potentially maybe 
    help us solve problems, and research indicates that it might be beneficial. Don't you 
    think this makes sense? What this means, in other words, is that we should obviously 
    collaborate to improve human connections and enhance cooperation between all conscious beings.
    """
    
    result = processor.process(verbose_text)
    
    print("UCP Processing Results:")
    print(f"Original length: {result['compression']['original_length']}")
    print(f"Compressed length: {result['compression']['compressed_length']}")
    print(f"Compression ratio: {result['compression']['compression_ratio']:.3f}")
    print(f"Enhancement score: {result['enhancement_score']:.3f}")
    print(f"Connection axiom valid: {result['connection_axiom_valid']}")
    print(f"Logical coherence: {result['compression']['logical_coherence']:.3f}")
    
    print("\nLogical chain extracted:")
    print(f"Premise: {result['logical_chain']['premise']}")
    print(f"Reasoning: {result['logical_chain']['reasoning']}")
    print(f"Conclusion: {result['logical_chain']['conclusion']}")
    
    return result

if __name__ == "__main__":
    demonstrate_ucp()