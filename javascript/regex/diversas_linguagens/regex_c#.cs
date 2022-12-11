using System.Text.RegularExpressions;
namespace ExemploRegex
{
    class Program
    {
        static void Main(string[] args)
        {
            string alvo = "12a34b56c";
            Regex regexp = new Regex(@"(\d\d)(\w)");

            MatchCollection resultados = regexp.Matches(alvo);
            foreach(Match resultado in resultados)
            {
                Console.WriteLine(string.Format("Resultado: {0}, Grupos: {1} e {2}, Index: [{3},{4}]", 
                    resultado.Value, 
                    resultado.Groups[1], 
                    resultado.Groups[2],
                    resultado.Index,
                    (resultado.Index+resultado.Length)));
                    Console.WriteLine("--------------");
            }
        }
    }
}