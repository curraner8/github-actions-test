try {
    // code that may throw an exception
    riskyOperation();
} catch(Exception e) {
    // VULNERABLE: Stack trace printed to default system output
    e.printStackTrace();
}

// SOURCE: https://docs.prismacloud.io/en/enterprise-edition/policy-reference/sast-policies/java-policies/sast-policy-138
