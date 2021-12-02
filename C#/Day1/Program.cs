

string inputPath = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile) + "\\git\\AOC-2021\\C#\\1\\Day1\\input.txt";
string[] fileText = System.IO.File.ReadAllLines(inputPath);



static uint part1(string[] input)
{
    uint larger = 0;

    for (int i = 0; i < input.Length - 1; i++)
    {
        ushort currentMeasurement = Convert.ToUInt16(input[i]);
        ushort nextMeasurement = Convert.ToUInt16(input[i + 1]);
        if (nextMeasurement > currentMeasurement)
        {
            larger++;
        }
    }
    return larger;
}


static uint part2(string[] input)
{
    uint largerWindows = 0;

    List<int> values = input.Select(int.Parse).ToList();

    for (int i = 0; i < input.Length - 3; i++)
    {
        List<int> currentWindow = values.GetRange(i, 3);
        List<int> nextWindow = values.GetRange(i + 1, 3);
        int currentWindowSum = currentWindow.Sum();
        int nextWindowSum = nextWindow.Sum();
        if (nextWindowSum > currentWindowSum)
        {
            largerWindows++;
        }
    }
    return largerWindows;
}

Console.WriteLine(part1(fileText));
Console.WriteLine(part2(fileText));