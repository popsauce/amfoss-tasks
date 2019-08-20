use regex::Regex;

// would integrate these after i solve my compilation error.
//let mut input = String::new();
//match io::stdin.read_line(&mut input)

//also thinking of matching top 10 most common domain names as they constitute more than 99% of email formats.


fn main()
{
let re = Regex::new(r"^([a-zA-z0-9_\-\.]+)@([a-zA-z0-9_\-\.])\.([a-zA-Z]{2,5})$").unwrap();
assert!(re.is_match("email@gmail.com"));
println!("email is valid")
}
