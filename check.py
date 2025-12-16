import os
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()
# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

def vulnerability_analyzer(code):
    """Analyze code for vulnerabilities and memory leaks"""
    prompt = (
        "You are a security expert and code analyst. Analyze the following code for:\n"
        "1. Security vulnerabilities (SQL injection, XSS, buffer overflow, etc.)\n"
        "2. Memory leaks and resource management issues\n"
        "3. Unsafe practices and potential exploits\n"
        "4. Input validation issues\n"
        "5. Error handling gaps\n\n"
        f"Code to analyze:\n{code}\n\n"
        "Provide a detailed report with:\n"
        "- Issue Type (Vulnerability/Memory Leak/Code Smell)\n"
        "- Severity (Critical/High/Medium/Low)\n"
        "- Location (line number if identifiable)\n"
        "- Description\n"
        "- Recommended Fix"
    )
    result = llm.invoke(prompt)
    return result

def generate_report(filename, analysis_result):
    """Generate a formatted security analysis report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = (
        f"{'='*80}\n"
        f"CODE SECURITY AND MEMORY ANALYSIS REPORT\n"
        f"{'='*80}\n"
        f"File Analyzed: {filename}\n"
        f"Analysis Date: {timestamp}\n"
        f"Analyzer: LLM-based Security Agent\n"
        f"{'='*80}\n\n"
        f"ANALYSIS RESULTS:\n"
        f"{'-'*80}\n"
        f"{analysis_result.content}\n"
        f"{'-'*80}\n"
        f"{'='*80}\n"
        f"END OF REPORT\n"
        f"{'='*80}\n"
    )
    
    return report

def save_report(filename, report_content):
    """Save the report to a file"""
    base_name = os.path.splitext(os.path.basename(filename))[0]
    report_filename = f"{base_name}_security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    return report_filename

def get_c_files(directory):
    """Get all C files in a directory recursively"""
    c_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".c") or file.endswith(".h"):
                c_files.append(os.path.join(root, file))
    
    return c_files

def analyze_file(filename):
    """Analyze a single file and return the report"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None
    
    print(f"Analyzing: {filename}")
    
    # Agent: Analyze code for vulnerabilities and memory leaks
    analysis = vulnerability_analyzer(content)
    
    # Generate formatted report
    report = generate_report(filename, analysis)
    
    # Save report to file
    report_filename = save_report(filename, report)
    print(f"  Report saved to: {report_filename}\n")
    
    return report_filename

def main():
    print("Code Vulnerability and Memory Leak Analyzer")
    print("=" * 50)
    
    # Get path from user
    path = input("Enter file path or directory path to analyze: ").strip()
    
    # Validate path exists
    if not os.path.exists(path):
        print(f"Error: Path '{path}' not found.")
        return
    
    # Handle single file
    if os.path.isfile(path):
        if not (path.endswith(".c") or path.endswith(".h")):
            print("Error: File must be a C source (.c) or header (.h) file.")
            return
        
        print(f"\nAnalyzing file: {path}")
        print(f"File size: {len(open(path).read())} characters\n")
        
        analyze_file(path)
    
    # Handle directory
    elif os.path.isdir(path):
        print(f"\nScanning directory: {path}")
        c_files = get_c_files(path)
        
        if not c_files:
            print("No C files (.c or .h) found in the directory.")
            return
        
        print(f"Found {len(c_files)} C file(s) to analyze.\n")
        print("=" * 50 + "\n")
        
        for c_file in c_files:
            analyze_file(c_file)
        
        print("=" * 50)
        print(f"Analysis complete. Processed {len(c_files)} file(s).")

if __name__ == "__main__":
    main()
