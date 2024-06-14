use std::collections::HashMap;
fn main() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    println!("{scores:?}");
    let team_name = "Blue".to_string();
    let score = scores.get(&team_name).copied().unwrap_or(0);
    println!("{score}");
    let team_name = "lue".to_string();
    let score = scores.get(&team_name).copied().unwrap_or(0);
    println!("{score}");
    for (key, value) in &scores {
        println!("{key}: {value}");
    }
    let fnm = "Favorite color".to_string();
    let fv = "Blue".to_string();
    let mut map = HashMap::new();
    map.insert(fnm, fv);
    //println!("{fnm}: {fv}"); //causes error, because key values are moved
    map.insert("Favorite color".to_string(), "Red".to_string()); //overwriting
    map.entry(String::from("Favorite color")).or_insert(String::from("green"));
    map.entry(String::from("Bad color")).or_insert(String::from("green"));
    println!("{map:?}");
    let text = "hello world wonderful world";
    let mut m = HashMap::new();
    for word in text.split_whitespace() {
        let count = m.entry(word).or_insert(0);
        *count += 1;
    }
    println!("{m:?}");
}
