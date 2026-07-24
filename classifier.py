def classify_ticket(subject, description):
    text = (subject + " " + description).lower()

    # Default values
    category = "General"
    priority = "Low"
    team = "Support Team"
    confidence = "85%"

    # Authentication issues
    if "login" in text or "password" in text or "account" in text:
        category = "Authentication"
        priority = "High"
        team = "Technical Support"
        confidence = "98%"

    # Billing issues
    elif "payment" in text or "refund" in text or "money" in text:
        category = "Billing"
        priority = "High"
        team = "Billing Team"
        confidence = "97%"

    # Bug issues
    elif "crash" in text or "bug" in text or "error" in text:
        category = "Bug Report"
        priority = "High"
        team = "Development Team"
        confidence = "96%"

    # Performance issues
    elif "slow" in text or "performance" in text:
        category = "Performance"
        priority = "Medium"
        team = "Technical Support"
        confidence = "95%"

    # Email issues
    elif "email" in text:
        category = "Email Issue"
        priority = "Medium"
        team = "Support Team"
        confidence = "94%"

    # Feature requests
    elif "feature" in text:
        category = "Feature Request"
        priority = "Low"
        team = "Product Team"
        confidence = "93%"

    return category, priority, team, confidence