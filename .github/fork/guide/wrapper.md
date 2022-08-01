# api wrapper
Pour vous faciliter la tache des apis warpper existes
<br>
module client instance exemple
```js
python
from discord.ext import commands
client = commands.Bot(command_prefix=['?'])
js
const DiscordJs = require('discord.js');
const bot = new DiscordJs.Client({ intents: 32767 });
Rust
use serenity::{
  async_trait,
  model::{channel::Message, gateway::Ready},
  prelude::*,
  Client
};
let mut client = Client::new(&token)
    .event_handler(Handler)
    .await;
Go
import (
  "github.com/bwmarrin/discordgo"
)
bot, err := discordgo.New("Bot " + os.Getenv("token"))
Java
import net.dv8tion.jda.api.JDABuilder;
CommandClientBuilder client = new CommandClientBuilder();
C#
client = new DiscordSocketClient();
```
