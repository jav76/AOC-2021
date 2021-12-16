using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;



namespace Day3
{
    public class Program
    {
        const string inputFile = @"..\..\..\..\input.txt";
        static string[] getInput(string fileName=inputFile)
        {
            return File.ReadAllLines(fileName);

        }
        static float[] commonBits(string[] input)
        {
            float[] bitSums = new float[input[0].Length];
            foreach (string line in input)
            {
                for (int i = 0; i < line.Length; i++)
                {
                    int currentBit = Convert.ToInt32(Char.GetNumericValue(line[i]));
                    bitSums[i] += currentBit;
                }
            }
            for (int i = 0; i < bitSums.Length; i++)
            {
                bitSums[i] = bitSums[i] / input.Length;
            }
            return bitSums;
        }
        static float[] commonBits(List<string> input)
        {
            float[] bitSums = new float[input[0].Length];
            foreach (string line in input)
            {
                for (int i = 0; i < line.Length; i++)
                {
                    int currentBit = Convert.ToInt32(Char.GetNumericValue(line[i]));
                    bitSums[i] += currentBit;
                }
            }
            for (int i = 0; i < bitSums.Length; i++)
            {
                bitSums[i] = bitSums[i] / input.Count;
            }
            return bitSums;
        }
        static int part1(string[] input)
        {
            string gammaRate = "";
            string epsilonRate = "";
            float[] bitSums = commonBits(input);
            foreach (float sum in bitSums)
            {
                if (sum >= 0.5)
                {
                    gammaRate += "1";
                    epsilonRate += "0";
                }
                else
                {
                    gammaRate += "0";
                    epsilonRate += "1";
                }
            }
            int powerConsumption = Convert.ToInt32(gammaRate, 2);
            powerConsumption *= Convert.ToInt32(epsilonRate, 2);
            return powerConsumption;
        }

        static int part2(string[] input)
        {
            List<string> oxygenRating = input.ToList();
            List<string> CO2Rating = input.ToList();
            int currentPosition = 0;
            while (oxygenRating.Count > 1)
            {
                float[] bitSums = commonBits(oxygenRating);
                foreach (string line in oxygenRating.ToList())
                {
                    int filterBit = 0;
                    if (bitSums[currentPosition] >= 0.5)
                    {
                        filterBit = 1;
                    }
                    int currentBit = Convert.ToInt32(Char.GetNumericValue(line[currentPosition]));
                    if (currentBit != filterBit)
                    {
                        oxygenRating.Remove(line);
                        if (oxygenRating.Count == 1)
                        {
                            break;
                        }
                    }
                }
                currentPosition++;
            }
            currentPosition = 0;
            while (CO2Rating.Count > 1)
            {
                float[] bitSums = commonBits(CO2Rating);
                foreach (string line in CO2Rating.ToList())
                {
                    int filterBit = 1;
                    if (bitSums[currentPosition] >= 0.5)
                    {
                        filterBit = 0;
                    }
                    int currentBit = Convert.ToInt32(Char.GetNumericValue(line[currentPosition]));
                    if (currentBit != filterBit)
                    {
                        CO2Rating.Remove(line);
                        if (CO2Rating.Count == 1)
                        {
                            break;
                        }
                    }
                }
                currentPosition++;
            }
            int finalOxygenRating = Convert.ToInt32(oxygenRating[0], 2);
            int finalCO2Rating = Convert.ToInt32(CO2Rating[0], 2);
            return finalOxygenRating * finalCO2Rating;

        }
        public static void Main(string[] args)
        {
            string[] lines = getInput();
            DateTime start1 = DateTime.Now;
            int solution1 = part1(lines);
            DateTime start2 = DateTime.Now;
            int solution2 = part2(lines);
            DateTime start3 = DateTime.Now;

            TimeSpan part1Time = start2 - start1;
            TimeSpan part2Time = start3 - start2;
            Console.WriteLine($"Part 1 solution: {solution1} in {part1Time.TotalMilliseconds}ms");
            // 2967914
            Console.WriteLine($"Part 2 solution: {solution2} in {part2Time.TotalMilliseconds}ms");
            // 7041258
        }
    }
}