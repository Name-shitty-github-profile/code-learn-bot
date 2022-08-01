Pour la data token et guild_id
<br>
Nous voulons un fichier different contenent ces informations
<br>
le token doit etre une variable environnement.
<br>
js
```js
process.env.VariableName
```
<br>
Go
```go
import (
  "os"
)
os.Getenv("VariableName")
```
<br>
Java
```java
System.getenv("VariableName");
```
<br>
c#
```c#
Environment.GetEnvironmentVariable("VariableName");
```
<br>
Rust
```rust
env::var("VariableName").unwrap()
```
