const palindromeNumber1 = (num: number): boolean => {
    let temp: number = num
    let revNum: number = 0
    while (temp > 0) {
        revNum = (revNum * 10) + (temp % 10);
        temp = Math.floor(temp / 10);
    }
    return num === revNum;
}

console.log(palindromeNumber1(1001));