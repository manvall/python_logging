# Logging in Python: Part 1 - Key Concepts, Examples, Configuration, and Best Practices
- [Logging in Python: Part 1 - Key Concepts, Examples, Configuration, and Best Practices](#logging-in-python-part-1---key-concepts-examples-configuration-and-best-practices)
  - [1. Introduction](#1-introduction)
  - [2. Key Concepts](#2-key-concepts)
    - [2.1 Log Levels](#21-log-levels)
    - [2.2 Logging Handlers](#22-logging-handlers)
    - [2.3 Log formatters](#23-log-formatters)
  - [3. Logging Configuration](#3-logging-configuration)
    - [3.1 Programmatic Configuration](#31-programmatic-configuration)
      - [1.Basic Configuration](#1basic-configuration)
      - [2. Advanced Configuration](#2-advanced-configuration)
      - [3. Dict Configuration](#3-dict-configuration)
    - [3.2 External Configuration Files](#32-external-configuration-files)
  - [5. Recommendations and Best Practices](#5-recommendations-and-best-practices)
  - [6. Conclusion](#6-conclusion)


## 1. Introduction
Logging is a crucial part of software development which allows developers to record errors, events and information while the program is running that can used for debugging, performance analysis, and monitoring. Python offers a built-in logging module that simplifies the process of implementing this.

In this Article, we will discuss on fundamental concepts of logging, different log levels available, and the power of handlers and how to format your logs. Additionally, we will also discuss on writing our own custom handlers and on how to configure logging, both programmatic and file based.

## 2. Key Concepts
### 2.1 Log Levels
Logging in Python is the process of assigning log messages different levels to indicate their importance or severity. The Python logging library offers several predefined log levels, including DEBUG, INFO, WARNING, ERROR, and CRITICAL. Understanding these log levels is crucial as they allow developers to assign the appropriate level to each log message. By doing so, the logs can provide the necessary information while avoiding unnecessary performance overhead in different environments.

- **DEBUG** (level 10): The `DEBUG` log level is used to provide detailed information during the debugging process. It is typically used for diagnostic purposes and is most useful during development and testing stages. Debug log messages often contain fine-grained information about the program's internal state, variable values, or function execution paths. However, it is important to note that `DEBUG` log messages are typically disabled in production environments to avoid excessive log output and potential performance overhead.

- **INFO** (level 20): The `INFO` log level is used for general information about the execution of the application. It provides high-level updates or progress indicators that can be useful for understanding the flow of the program. Info log messages may include status updates, configuration details, or important milestones reached during the application's execution.

- **WARNING** (level 30): The `WARNING` log level indicates potential issues or anomalies that may require attention. It signifies situations where the application might be functioning as expected, but there could be a problem or a configuration that warrants investigation. Warning log messages often highlight non-critical errors, deprecated functionalities, or unusual scenarios that could impact the application's behavior.

- **ERROR** (level 40): The `ERROR` log level represents errors or exceptions that occurred during the application's execution. These log messages indicate that an unexpected condition has occurred, but it is not severe enough to terminate the application. Error log messages often capture exceptions, failures in critical operations, or unexpected behavior that needs to be addressed. By logging errors, developers can track down issues and take corrective actions.

- **CRITICAL** (level 50): The `CRITICAL` log level signifies critical errors or severe failures that might lead to the termination of the application. Critical log messages are reserved for exceptional conditions that require immediate attention. They represent situations where the application's functionality is compromised, and the system might be in an unstable state. These log messages often indicate failures in essential operations, system-level errors, or security-related incidents.

In addition to their names, each log level also has a corresponding numerical value. These numerical values follow an increasing order of severity, allowing for programmatic comparisons and filtering based on the level of importance.

```python

import logging

logging.basicConfig(level=logging.DEBUG) 

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

```

**Output:**
```
DEBUG: This is a debug message
INFO: This is an info message
WARNING: This is a warning message
ERROR: This is an error message
CRITICAL: This is a critical message
```


Note that the logging level can be set using the `basicConfig` method. In the above example, the level is set to `DEBUG` to include all log messages for propagation. Messages below this level will be ignored by the logger. We will explore more about  using the basicConfig method in later sections.


> There is a special log level called **NOTSET**, which has a value of 0. This level serves as a default and is typically not used to assign a specific level to log messages. Instead, it acts as a placeholder to indicate that the logging level has not been explicitly set for a logger or a handler.
> 
> When the logging level is set to *NOTSET*, it does not filter any log messages. Instead, it allows all log messages, regardless of their level, to be processed. Log messages with a level greater than zero (including DEBUG, INFO, WARNING, ERROR, and CRITICAL) will be propagated.

### 2.2 Logging Handlers
Log handlers are components of the logging system that handle the writing of log messages to different destinations. Python's built-in logging library offers a range of log handlers that developers can utilize based on their requirements. Some commonly used log handlers include:

- **StreamHandler:** This handler sends log messages to a stream, typically the console or standard output. It is useful for displaying logs in real-time during development or when running scripts interactively.

- **FileHandler:** The FileHandler writes log messages to a file. It enables developers to store logs in a specific file location for later analysis or archival purposes.
  
- **RotatingFileHandler:** Similar to the FileHandler, the RotatingFileHandler includes additional functionality to manage log files that rotate based on criteria like file size or time intervals. It proves beneficial when dealing with large volumes of logs.

- **SMTPHandler:** The SMTPHandler sends log messages via email. It allows developers to receive log notifications directly in their email inbox, making it convenient for critical error alerts or system monitoring.
  
In addition to the built-in handlers, developers can also create their own custom handlers to cater to specific logging needs.

By leveraging these logging handlers, developers have the ability to control where log messages are directed, ensuring logs are stored, displayed, or delivered to the appropriate destinations as per the application's requirements.

```Python
import logging

logging.basicConfig(level=logging.DEBUG)

# Create log handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')
rotating_handler = logging.handlers.RotatingFileHandler('app_rotating.log')

# Create a logger and add the created to log handlers.
logger = logging.getLogger('my_logger')
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(rotating_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

```

Each of these handlers can be assigned it's own log level. When a handler is writing any log, it ignores all the messages that hre of lower level than it's own level. For example, if we configure the **file_handler** in the above example with *warning* level, any logs below warning level are ignored and would not be written to a file.

```Python
import logging

logging.basicConfig(level=logging.DEBUG)


file_handler = logging.FileHandler('app.log')


# Create a logger and add the created to log handlers.
logger = logging.getLogger('my_logger')
logger.addHandler(file_handler)

# Log some messages
logger.debug('This is a debug message') # -> this will be ignored
logger.info('This is an info message') # -> this will be ignored
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

```
**Output:**

**app.log** file:
```
WARNING: This is a warning message
ERROR: This is an error message
CRITICAL: This is a critical message
```

### 2.3 Log formatters
Log formatters in Python's logging library are responsible for defining the structure and layout of log messages. They specify the format in which log messages are displayed or stored. Python's logging library offers flexible formatting options, allowing developers to customize the log format by specifying various attributes such as timestamp, log level, module name, and the actual log message itself. A comprehensive list of these attributes can be found in the [Python documentation](https://docs.python.org/3/library/logging.html#logrecord-attributes).

By using log formatters, developers have control over the presentation of log messages, making them more readable, informative, and consistent. Log formatters are typically associated with log handlers, allowing developers to format log messages based on the destination or output medium. For example, log messages can be formatted in JSON format when writing logs to files, facilitating better parsing and analysis. Alternatively, log messages can be formatted in a string format to enhance human readability.

This capability of log formatters to format log messages according to specific requirements enables developers to optimize log output for various scenarios, ensuring that log messages are well-suited for downstream processing, analysis, machine or human consumption.

```Python
import logging

# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler and set the log format
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)

# Below format will be used writing logs.
my_format = '%(asctime)s - %(levelname)s - %(message)s'

formatter = logging.Formatter(my_format) 
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log some messages

# debug and info levels will be ignored due to the setting of WARNING level
logger.debug('This is a debug message') 
logger.info('This is an info message')

# These levels will be propagated.
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

**Output:**

*app.log* file
```
2023-07-13 13:14:11,759 - WARNING - This is a warning message
2023-07-13 13:14:11,759 - ERROR - This is an error message
2023-07-13 13:14:11,759 - CRITICAL - This is a critical message
```

Try to modify the format and experiment with different placeholders and formatting options based on your specific requirements.


## 3. Logging Configuration
Now that we have a solid understanding of these key concepts, let's move on to the configuration options available in Python's logging system. Configuration enables us to fine-tune the logging behavior, specify output destinations, define log formats, and more.

### 3.1 Programmatic Configuration 
 
#### 1.Basic Configuration
The [`logging.basicConfig`](https://docs.python.org/3/library/logging.html#logging.basicConfig) method provides a simple way to configure logging using default settings. This method accepts several parameters, including the logging level, log format, output destination, and more.

**Logging to Console:**
```Python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
```

**Output:**
```
2023-07-13 13:33:29,596 - DEBUG - This is a debug message
2023-07-13 13:33:29,597 - INFO - This is an info message
2023-07-13 13:33:29,597 - WARNING - This is a warning message
2023-07-13 13:33:29,597 - ERROR - This is an error message
2023-07-13 13:33:29,597 - CRITICAL - This is a critical message
```


**Logging to File:**
```Python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'
)
```

**Output:**

***app.log*** file
```
2023-07-13 13:33:29,596 - DEBUG - This is a debug message
2023-07-13 13:33:29,597 - INFO - This is an info message
2023-07-13 13:33:29,597 - WARNING - This is a warning message
2023-07-13 13:33:29,597 - ERROR - This is an error message
2023-07-13 13:33:29,597 - CRITICAL - This is a critical message
```

> Note that by default, `logging.basicConfig` creates a *StreamHandler* to write logs to console. However, if filename argument is passed, it creates a FileHandler instead of StreamHandler.


#### 2. Advanced Configuration
For more advanced logging configuration, Python's logging module provides additional options. This includes configuring multiple loggers, using different log handlers, setting up loggers hierarchy, configuring log filtering, and more.

```Python
import logging

# Create loggers
logger1 = logging.getLogger('module1')
logger2 = logging.getLogger('module2')

# Create handlers
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler('logger2.log')

# Set log levels to each logger
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.INFO)

# Set log levels and formats to each handler
handler1.setLevel(logging.DEBUG)
handler2.setLevel(logging.INFO)

formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(levelname)s: %(message)s @ %(asctime)s')

handler1.setFormatter(formatter1)
handler2.setFormatter(formatter2)

# Add handlers to loggers
logger1.addHandler(handler1)
logger2.addHandler(handler2)

logger1.debug("This is Debug message from logger1")
logger1.info("This is Info message from logger1")

logger2.debug("This is Debug message from logger2") # -> This would not be propagated due to log level
logger2.info("This is Info message from logger2")
```

The above code results in a file named *logger2.log* and some messages logged to console.

**Console Output:**
```
2023-07-13 13:52:56,256 - DEBUG - This is Debug message from logger1
2023-07-13 13:52:56,256 - INFO - This is Info message from logger1
```

**File Output:**

logger2.log
```
INFO: This is Info message from logger2 @ 2023-07-13 13:52:56,256
```

#### 3. Dict Configuration
Python's logging module also supports configuration using a dictionary-based configuration using [`logging.dictConfig`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig). Let's configure the above example using dictConfig method.

```Python
import logging.config


configuration_dictionary = {
    "version": 1,
    "formatters": {
        "formatter1": {"format": "%(asctime)s - %(levelname)s - %(message)s"},
        "formatter2": {"format": "%(levelname)s: %(message)s @ %(asctime)s"},
    },
    "handlers": {
        "handler1": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "formatter1",
            "stream": "ext://sys.stdout",
        },
        "handler2": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "formatter2",
            "filename": "logger2_with_dict_config.log",
        },
    },
    "loggers": {
        "logger1": {"level": "DEBUG", "handlers": ["handler1"]},
        "logger2": {"level": "INFO", "handlers": ["handler2"]},
    },
}

logging.config.dictConfig(configuration_dictionary)


logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

logger1.debug("This is Debug message from logger1")
logger1.info("This is Info message from logger1")

logger2.debug("This is Debug message from logger2")
logger2.info("This is Info message from logger2")
```

**Console Output:**
```
2023-07-13 14:45:13,164 - DEBUG - This is Debug message from logger1
2023-07-13 14:45:13,164 - INFO - This is Info message from logger1
```

**File Output:**

logger2_with_dict_config.log
```
INFO: This is Info message from logger2 @ 2023-07-13 14:45:13,164
```

As shown above, multiple formatter, handlers and logger can be created and assigned as required.


### 3.2 External Configuration Files
In the above section we saw how to configure logging within the program script. Here, we will see how to use external files to configure logging. This can be helpful in separating the configuration from code.

External configuration files can be written in various formats, including INI-style, TOML,JSON, or YAML. The logging module provides the [`logging.fileConfig`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig) method to read the configuration, which uses [`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser) functionality,  from an external file and apply it to the logging system. However, this method is an older API and no is no longer getting any added functionality. Another way to use file based configuration is to manually read the file and call `logging.dictConfig` on it. Let's see an example on how to do it with the same configuration used above.

> We need to have [PyYAML](https://pypi.org/project/PyYAML/) installed to read the yaml file.

**logging_config.yaml**:
```Yaml
version: 1
formatters:
  formatter1:
    format: "%(asctime)s - %(levelname)s - %(message)s"
  formatter2:
    format: "%(levelname)s: %(message)s @ %(asctime)s"
handlers:
  handler1:
    class: logging.StreamHandler
    level: DEBUG
    formatter: formatter1
    stream: ext://sys.stdout
  handler2:
    class: logging.FileHandler
    level: INFO
    formatter: formatter2
    filename: logger2_with_dict_config.log
loggers:
  logger1:
    level: DEBUG
    handlers: [handler1]
  logger2:
    level: INFO
    handlers: [handler2]
```

```Python
import logging.config
import yaml

with open("logging_config.yaml", "r") as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

logger1.debug("This is Debug message from logger1")
logger1.info("This is Info message from logger1")

logger2.debug("This is Debug message from logger2")
logger2.info("This is Info message from logger2")
```

Similarly, we can read configuration files in other formats and create the corresponding dictionary structure to configure logging using the dictConfig method.

## 5. Recommendations and Best Practices

Logging is a powerful tool for troubleshooting, debugging, and monitoring processes. However, the usefulness of logs depends on the quality and format of the log content. Logs that display unnecessary or uninformative information are a waste of resources. So, let's discuss some best practices to follow:
- **Use Appropriate Log Levels:** Assign log levels based on the severity or importance of the logged events. Use levels like DEBUG, INFO, WARNING, ERROR, and CRITICAL to accurately convey the significance of each message.
- **Log Only Relevant Information:**  Include only essential and pertinent details in log messages. Avoid logging excessive or trivial information that does not contribute to problem diagnosis or system analysis. Focus on timestamps, log levels, and meaningful messages that provide insights into the system's state.
- **Use Appropriate Structured Logging:** Structure log messages in a clear format that suits the intended consumers. Consider using a format like JSON for machine-readable logs, but ensure readability for human consumption as well.
- **Separate Configuration from code:** Decouple logging configuration from source code by using file-based configurations. This allows for easier configuration changes without modifying the code itself.
- **Do Not log sensitive information:** Be careful not to log sensitive data such as credentials, secrets, or API keys as this could pose security risks.
- **Log All Errors:** Log all errors encountered, especially in production environments where logs may be the primary source of information. Consider logging the original error along with any subsequent errors raised for better troubleshooting and analysis.

## 6. Conclusion
In this article, we have explored the key concepts of logging in Python, including log levels, log handlers, and log formatters. We learned how log levels allow us to categorize and prioritize log messages, while log handlers determine where the log messages are written. Log formatters provide the ability to control the presentation and structure of log messages.

We also looked into the configuration options available in Python's logging module, starting with basic configuration using basicConfig and advancing to more advanced configuration techniques such as multiple loggers, handlers, and external configuration files.

Looking ahead, in the next part, we will delve into using the structlog library to enhance our logging. structlog library provides additional features and flexibility for logging, allowing us to enrich our logs with contextual information, structured data, and custom log processors.
