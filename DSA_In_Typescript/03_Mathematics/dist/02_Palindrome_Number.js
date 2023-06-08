const palindromeNumber1 = (num) => {
    let temp = num;
    let revNum = 0;
    while (temp > 0) {
        revNum = (revNum * 10) + (temp % 10);
        temp = Math.floor(temp / 10);
    }
    return num === revNum;
};
console.log(palindromeNumber1(1001));
