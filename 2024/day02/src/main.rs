use std::fs;

fn solve_p1(input: Vec<Vec<i32>>) {
    let mut count = 0;

    for val in input {
        let mut is_increase = true;
        let mut is_decrease = true;
        let mut is_valid = true;

        for i in 1..val.len() {
            if val[i] > val[i - 1] {
                is_decrease = false;
            }
            if val[i] < val[i - 1] {
                is_increase = false;
            }
            if (val[i] - val[i - 1]).abs() < 1 || (val[i] - val[i - 1]).abs() > 3 {
                is_valid = false;
            }
        }

        if (is_decrease && is_valid) || (is_increase && is_valid) {
            count += 1;
        }
    }

    println!("Answer for Part 1: {}", count);
}

fn solve_p2(input:  Vec<Vec<i32>>) {
    let mut count = 0;

    for val in input {
        for i in 0..=val.len() {
            let mut is_increase = true;
            let mut is_decrease = true;
            let mut is_valid = true;

            let mut temp = val.clone();
            if i != val.len() {
                temp.remove(i);
            }

            for j in 1..temp.len() {
                if temp[j] > temp[j - 1] {
                    is_decrease = false;
                }
                if temp[j] < temp[j - 1] {
                    is_increase = false;
                }
                if (temp[j] - temp[j - 1]).abs() < 1 || (temp[j] - temp[j - 1]).abs() > 3 {
                    is_valid = false;
                }
            }

            if (is_decrease && is_valid) || (is_increase && is_valid) {
                count += 1;
                break;
            }
        }
    }

    println!("Answer for Part 2: {}", count);
}

fn main() {
    let input = fs::read_to_string("./in.txt").unwrap();
    let lines = input.lines().collect::<Vec<_>>();

    let ints: Vec<Vec<i32>> = lines.iter().map(|a| a.split_whitespace().map(|b| b.parse().unwrap()).collect()).collect();

    solve_p1(ints.clone());
    solve_p2(ints);
}