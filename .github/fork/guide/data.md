Pour la data token et guild_id
<br>
Nous voulons un fichier different contenent ces informations
<br>
le token doit etre une variable environnement.
<br>
js<br>
```js
process.env.VariableName
```
<br>
Go<br>
```go
import (
  "os"
)
os.Getenv("VariableName")
```
<br>
Java<br>
```java
System.getenv("VariableName");
```
<br>
c#<br>
```c#
Environment.GetEnvironmentVariable("VariableName");
```
<br>
Rust<br>
```rust
env::var("VariableName").unwrap()
```
