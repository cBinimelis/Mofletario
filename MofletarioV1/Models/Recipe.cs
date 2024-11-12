using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Mofletario.Models;

public class Recipe
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public string? Description { get; set; }
    public DateTime PublishDate { get; set; } = System.DateTime.Now;
    public int PreparationTime { get; set; }
    public int CookTime { get; set; }
    public int Portions { get; set; }
    public int DificultyLevel { get; set; }
    public int CaloriesPerServing { get; set; }
    public string? Image { get; set; }
}
