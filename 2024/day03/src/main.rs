use std::fs;
use regex::Regex;

fn solve_p1(input: String) {
    let re: Regex = Regex::new(r"mul\([0-9]+,[0-9]+\)").unwrap();
    let parse = re.find_iter(&input).map(|m| m.as_str()).collect::<Vec<_>>();

    let mut res = 0;
    for i in parse {
        let split: Vec<_> = i.split(',').collect();
        let first: i32 = split[0].split('(').collect::<Vec<_>>()[1].parse().unwrap();
        let second: i32 = split[1].split(')').collect::<Vec<_>>()[0].parse().unwrap();
        res = res + (first * second);
    }
    println!("Answer for Part 1: {}", res);
}

fn solve_p2(input: String) {
    let re: Regex = Regex::new(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))").unwrap();
    let parse = re.find_iter(&input).map(|m| m.as_str()).collect::<Vec<_>>();

    let mut res = 0;
    let mut is_on = true;

    for i in parse {
        if i == "do()" {
            is_on = true;
        } else if i == "don't()" {
            is_on = false;
        }

        if is_on && i.starts_with("mul") {
            let split: Vec<_> = i.split(',').collect();
            let first: i32 = split[0].split('(').collect::<Vec<_>>()[1].parse().unwrap();
            let second: i32 = split[1].split(')').collect::<Vec<_>>()[0].parse().unwrap();
            res = res + (first * second);
        }
    }

    println!("Answer for Part 2: {}", res);
}

fn main() {
    let input = fs::read_to_string("./in.txt").unwrap();

    solve_p1(input.clone());
    solve_p2(input);
}