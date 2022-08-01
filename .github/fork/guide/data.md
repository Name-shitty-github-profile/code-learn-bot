Pour la data token et guild_id
<br>
Nous voulons un fichier different contenent ces informations
<br>
le token doit etre une variable environnement.
<br>
```js
Js
process.env.VariableName
Go
import (
  "os"
)
os.Getenv("VariableName")
Java
System.getenv("VariableName");
C#
Environment.GetEnvironmentVariable("VariableName");
Rust
env::var("VariableName").unwrap()
```
