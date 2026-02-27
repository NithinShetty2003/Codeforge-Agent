def calculate_score(results):
    weights = {
        "bug_detection": 3000,
        "security": 2000,
        "refactoring": 2000,
        "architecture": 1500,
        "structure": 1500
    }

    score = 0

    score += results.get("bug_detection", 0) * weights["bug_detection"]
    score += results.get("security", 0) * weights["security"]
    score += results.get("refactoring", 0) * weights["refactoring"]
    score += results.get("architecture", 0) * weights["architecture"]
    score += results.get("structure", 0) * weights["structure"]

    return int(score)