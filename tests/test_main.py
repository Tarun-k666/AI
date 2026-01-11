"""Tests for main module"""

from src.main import hello_ai


def test_hello_ai():
    """Test the hello_ai function"""
    result = hello_ai()
    assert result == "AI Project Ready"
