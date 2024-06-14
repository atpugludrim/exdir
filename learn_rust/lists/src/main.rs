#[derive(Debug)]
enum SpreadsheetCell{
    Int(i32),
    Float(f64),
    Text(String),
}
fn main() {
    let v: Vec<i32> = Vec::new();
    println!("{v:?}");
    let v = vec![1, 2, 3];
    println!("{v:?}");
    let mut v = Vec::new();
    v.push(5);
    v.push(6);
    v.push(7);
    println!("{v:?}");
    let third: &i32 = &v[2];
    println!("The third element is {third}");
    let third: Option<&i32> = v.get(5);
    match third {
        Some(third) => println!("The third element is {third}"),
        None => println!("There is no third element."),
    }
    for i in &v {
        println!("{i}")
    }
    for i in &mut v {
        *i += 50;
    }
    println!("{v:?}");
    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];
    println!("{row:?}");
}
