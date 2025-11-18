def require_non_empty(value, label="Field"):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{label} cannot be empty")
