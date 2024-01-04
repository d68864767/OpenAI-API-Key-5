```python
# Importing necessary libraries
from what_if_tool import WhatIfTool
from captum import Captum
from eli5 import ELI5
from debugging_ai_decisions import DebuggingAIDecisions

def main():
    # Initialize the debugging tools
    what_if_tool = WhatIfTool()
    captum = Captum()
    eli5 = ELI5()
    debugging_ai_decisions = DebuggingAIDecisions()

    # Use the debugging tools on your AI model
    what_if_tool.debug_model()
    captum.debug_model()
    eli5.debug_model()
    debugging_ai_decisions.debug_model()

if __name__ == "__main__":
    main()
```
