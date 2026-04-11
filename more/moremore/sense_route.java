# VULNERABLE: Exposes all actuator endpoints without authentication
management.endpoints.web.exposure.include=*
management.endpoints.web.base-path=/actuator

# Also vulnerable for older Spring Boot versions
management.security.enabled=false

# SOURCE:  https://codeql.github.com/codeql-query-help/java/java-spring-boot-exposed-actuators-config/
