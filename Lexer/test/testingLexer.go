package main

import (
	"flag"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"myproject/Lexer/lexer"
)

func main() {
	// Define a command line flag named "input" with a default value of "input.txt"
	inputFileName := flag.String("input", "input.txt", "Input file name")
	flag.Parse()

	// Retrieve the value of the "input" flag
	fileName := *inputFileName

	// Check if the file exists
	if _, err := os.Stat(fileName); os.IsNotExist(err) {
		fmt.Printf("File %s does not exist\n", fileName)
		return
	}

	// Open the input file for reading
	inputFile, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("Error opening file: %v\n", err)
		return
	}
	defer inputFile.Close()

	// Read the contents of the input file
	content, err := io.ReadAll(inputFile)
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	inputS := string(content)
	l := lexer.New(inputS)
	// Construct the output file name
	outputFileName := "output_" + filepath.Base(fileName)

	// Open the output file for writing
	outputFile, err := os.Create(outputFileName)
	if err != nil {
		fmt.Printf("Error creating file: %v\n", err)
		return
	}
	defer outputFile.Close()
	for {
		tok := l.NextToken()
		fmt.Printf("%+v\n", tok)
		_, err = fmt.Fprintf(outputFile, "%+v\n", tok)
		if err != nil {
			fmt.Println("Error writing to file:", err)
			return
		}
		if tok.Type == "EOF" {
			break
		}
	}
	// Write the contents to the output file
	// _, err = outputFile.Write(content)
	if err != nil {
		fmt.Printf("Error writing to file: %v\n", err)
		return
	}

	fmt.Printf("Contents of %s written to %s\n", fileName, outputFileName)
}
