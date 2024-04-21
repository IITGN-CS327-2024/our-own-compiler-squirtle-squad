package main

import (
	"flag"
	"fmt"
	"io"
	"myproject/Lexer/lexer"
	"os"
	"path/filepath"
)

func main() {
	// Define command line flags
	inputFileName := flag.String("input", "input.txt", "Input file name")
	outputFilePath := flag.String("output", "", "Output file path")
	flag.Parse()

	// Retrieve the values of the flags
	fileName := *inputFileName
	outputPath := *outputFilePath

	// Check if the input file exists
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

	// Construct the output file path
	outputFileName := filepath.Join(outputPath, "output_"+filepath.Base(fileName))

	// Open the output file for writing
	outputFile, err := os.Create(outputFileName)
	if err != nil {
		fmt.Printf("Error creating file: %v\n", err)
		return
	}
	defer outputFile.Close()

	for {
		
		tok := l.NextToken()

		if tok.Type == "Mod" {
			temp := "Mod,%%\n"
			_, err = fmt.Fprintf(outputFile, temp)
		} else {
			formatted := fmt.Sprintf("%s,%s\n", tok.Type, tok.Literal)

			_, err = fmt.Fprintf(outputFile, formatted)
		}
		if err != nil {
			fmt.Println("Error writing to file:", err)
			return
		}
		if tok.Type == "EOF" {
			break
		}
		
		
	}

	fmt.Printf("Contents of %s written to %s\n", fileName, outputFileName)
}
