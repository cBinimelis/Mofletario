using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Mofletario.Models;

namespace Mofletario.Data
{
    public class MofletarioContext : DbContext
    {
        public MofletarioContext (DbContextOptions<MofletarioContext> options)
            : base(options)
        {
        }

        public DbSet<Mofletario.Models.Recipe> Recipe { get; set; } = default!;
    }
}
