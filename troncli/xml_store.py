logback = r"""<?xml version="1.0" encoding="UTF-8"?>

<configuration>

  <!-- Be sure to flush latest logs on exit -->
  <shutdownHook class="ch.qos.logback.core.hook.DelayingShutdownHook"/>

  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
  <encoder>
  <pattern>%d{HH:mm:ss.SSS} %-5level [%t] [%c{1}]\(%F:%L\) %m%n</pattern>
  </encoder>
  <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
  <level>INFO</level>
  </filter>
  </appender>

  <appender name="FILE"
    class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>./logs/tron.log</file>
    <rollingPolicy
      class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
      <!-- rollover daily -->
      <fileNamePattern>./logs/tron-%d{yyyy-MM-dd}.%i.log.gz</fileNamePattern>
      <!-- each file should be at most 500MB, keep 30 days worth of history, but at most 50GB -->
      <maxFileSize>500MB</maxFileSize>
      <maxHistory>3</maxHistory>
      <totalSizeCap>50GB</totalSizeCap>
    </rollingPolicy>
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} %-5level [%t] [%c{1}]\(%F:%L\) %m%n</pattern>
    </encoder>
    <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
      <level>TRACE</level>
    </filter>
  </appender>

  <appender name="ASYNC" class="ch.qos.logback.classic.AsyncAppender">
    <!-- Don't discard INFO, DEBUG, TRACE events in case of queue is 80% full -->
    <discardingThreshold>0</discardingThreshold>
    <!-- Default is 256 -->
    <!-- Logger will block incoming events (log calls) until queue will free some space -->
    <!-- (the smaller value -> flush occurs often) -->
    <queueSize>100</queueSize>
    <includeCallerData>true</includeCallerData>
    <appender-ref ref="FILE"/>
  </appender>

  <root level="INFO">
    <appender-ref ref="STDOUT"/>
    <appender-ref ref="ASYNC"/>
  </root>

  <logger name="app" level="INFO"/>
  <logger name="net" level="INFO"/>
  <logger name="backup" level="INFO"/>
  <logger name="discover" level="INFO"/>
  <logger name="crypto" level="INFO"/>
  <logger name="utils" level="INFO"/>
  <logger name="actuator" level="INFO"/>
  <logger name="API" level="INFO"/>
  <logger name="witness" level="INFO"/>
  <logger name="DB" level="INFO"/>
  <logger name="capsule" level="INFO"/>
  <logger name="VM" level="INFO"/>

</configuration>
"""