fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
fn main() {
    let mut s = String::new();
    let data = "initial contents";
    print_type_of(&s);
    print_type_of(&data);
    print_type_of(&data.to_string());
    println!("{data:?}");
    s.push_str("Yamete");
    println!("{s}");
    let s = String::from("initial contents");
    println!("{s}");
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s = s1 + &s2; // s1 has been moved and can no longer be used
    println!("{s}");
    let s = s + "-" + &s2 + "-";
    println!("{s}");
    let s = format!("{s}-{s2}-");
    println!("{s}");
    let h = &s[0..1];
    println!("{h}");
    for c in s2.chars() {
        /*let s = String::from(c);
        println!("s: {s}");
        print_type_of(&s);*/
        print_type_of(&c);
        println!("{c}");
    }
    for c in s2.bytes() {
        println!("{c}");
    }
}
