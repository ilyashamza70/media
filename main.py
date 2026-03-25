#!/usr/bin/env python3
"""
Main entry point for the Grade Calculator application.
This script allows running the application from the project root.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from grade_calculator import main

if __name__ == "__main__":
    main()
