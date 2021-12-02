



string inputPath = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile) + "\\git\\AOC-2021\\C#\\Day2\\input.txt";
string[] fileText = System.IO.File.ReadAllLines(inputPath);


static int part1(string[] input)
{
    int position = 0;
    int depth = 0;
    foreach (string line in input)
    {
        string[] split = line.Split(' ');
        string direction = split[0];
        int value = int.Parse(split[1]);

        switch (direction)
        {
            case "forward":
                position = position + value;
                break;

            case "down":
                depth = depth + value;
                break;

            case "up":
                depth = depth - value;
                break;

            default:
                break;
        }
    }
    return depth * position;
}

static int part2(string[] input)
{
    int position = 0;
    int depth = 0;
    int aim = 0;
    foreach (string line in input)
    {
        string[] split = line.Split(' ');
        string direction = split[0];
        int value = int.Parse(split[1]);

        switch (direction)
        {
            case "forward":
                position = position + value;
                depth = depth + aim * value;
                break;

            case "down":
                aim = aim + value;
                break;

            case "up":
                aim = aim - value;
                break;

            default:
                break;
        }
    }
    return depth * position;
}

Console.WriteLine(part1(fileText));
Console.WriteLine(part2(fileText));