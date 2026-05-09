def main():
    score = 0

    print("=====================================")
    print("      STOCK MARKET EXPERT SYSTEM (AI)")
    print("=====================================")

    # INPUT SECTION
    print("\nMarket Trend:")
    print("1. Rising\n2. Falling\n3. Stable")
    trend = int(input("Enter choice: "))

    print("\nPrice Level:")
    print("1. Low\n2. Medium\n3. High")
    price = int(input("Enter choice: "))

    print("\nRisk Level:")
    print("1. Low Risk\n2. Medium Risk\n3. High Risk")
    risk = int(input("Enter choice: "))

    print("\nTrading Volume:")
    print("1. Low\n2. Medium\n3. High")
    volume = int(input("Enter choice: "))

    print("\nAnalyzing Market Conditions...\n")

    # KNOWLEDGE BASE (RULES)
    # Trend Rules
    if trend == 1:
        print("Rule Applied: Rising Market (+2)")
        score += 2
    elif trend == 2:
        print("Rule Applied: Falling Market (-2)")
        score -= 2
    else:
        print("Rule Applied: Stable Market (+0)")

    # Price Rules
    if price == 1:
        print("Rule Applied: Low Price (+2)")
        score += 2
    elif price == 3:
        print("Rule Applied: High Price (-2)")
        score -= 2

    # Risk Rules
    if risk == 1:
        print("Rule Applied: Low Risk (+1)")
        score += 1
    elif risk == 3:
        print("Rule Applied: High Risk (-1)")
        score -= 1

    # Volume Rules
    if volume == 3:
        print("Rule Applied: High Volume (+1)")
        score += 1
    elif volume == 1:
        print("Rule Applied: Low Volume (-1)")
        score -= 1

    # FINAL DECISION
    print(f"\nFinal Score: {score}")

    if score >= 3:
        print("Decision: BUY (Strong Positive Signal)")
    elif score >= 1:
        print("Decision: HOLD (Moderate Market)")
    else:
        print("Decision: SELL (Negative Market)")

    print()


if __name__ == "__main__":
    main()
