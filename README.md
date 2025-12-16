# Vulnerability Checker Agent

An AI powered security analysis tool that scans C source code for vulnerabilities and memory leaks using LLM based code analysis.

Repository: https://github.com/Lightmean03/vuln-checker-Agent.git

## Overview

This tool analyzes C code files for security vulnerabilities, memory leaks, unsafe practices, input validation issues, and error handling gaps. It can process individual files or entire directories and generates detailed security reports for each file analyzed.

## Features

Single File Analysis: Analyze individual C or header files
Directory Scanning: Process all C files in a directory recursively
Comprehensive Reports: Detailed security analysis with severity levels
Automated Report Generation: Reports are saved with timestamps for easy tracking
Severity Classification: Issues are marked as Critical, High, Medium, or Low

## Installation

Clone the repository:

```bash
git clone https://github.com/Lightmean03/vuln-checker-Agent.git
cd vuln-checker-Agent
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Set up your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Run the analyzer:

```bash
python check.py
```

The program will prompt you to enter a path. You can provide either:

A single file path: Analyzes that specific C file
A directory path: Scans and analyzes all C files (.c and .h) in that directory and subdirectories

## Report Output

Reports are generated for each analyzed file with the naming format:

```
{filename}_security_report_{timestamp}.txt
```

Each report includes:

File name and analysis timestamp
Identified vulnerabilities and memory leaks
Severity levels for each issue
Specific locations of problems
Recommended fixes

## Analysis Categories

The tool checks for the following:

Security vulnerabilities including SQL injection, XSS, buffer overflow
Memory leaks and resource management issues
Unsafe coding practices and potential exploits
Input validation problems
Error handling gaps

## Requirements

Python 3.8 or higher
OpenAI API key with access to gpt-4o-mini model
LangChain library
DuckDuckGo search integration

