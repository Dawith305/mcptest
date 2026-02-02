function getAdultUserNames(users, defaultMessage = "No users over 18.") {
    const adultNames = users
      .filter(user => typeof user.age === "number" && user.age > 18)
      .map(user => String(user.name).trim())
      .filter(name => name.length > 0);
  
    if (adultNames.length === 0) {
      return defaultMessage;
    }
  
    return adultNames.join(", ");
  }

  const users = [
    { name: "Alice", age: 20 },
    { name: "Bob", age: 17 },
    { name: "Charlie", age: 25 },
  ];
  
  console.log(getAdultUserNames(users));