#!/usr/bin/env python3
import time
from datetime import datetime
import sys

try:
    import anthropic
except ImportError:
    print("[ERROR] anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)


def health_check():
    """Call the Anthropic API and log health status."""
    timestamp = datetime.utcnow().isoformat() + "Z"
    start_time = time.time()

    try:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=10,
            messages=[{"role": "user", "content": "ping"}],
        )
        response_time = time.time() - start_time
        print(f"[{timestamp}] Health check: OK (response_time={response_time:.3f}s)")
        return True
    except Exception as e:
        response_time = time.time() - start_time
        print(f"[{timestamp}] Health check: FAILED (error={str(e)}, response_time={response_time:.3f}s)")
        return False


if __name__ == "__main__":
    success = health_check()
    sys.exit(0 if success else 1)
