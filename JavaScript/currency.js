fetch('https://api.twitter.com/')
  .then(response => response.json())
  .then(data => {
    const query = 'victor'
    const search = data.search[query]

    if (search) {
      console.log(search)
    } else {
      console.log('Invalid query!')
    }
  })
  .catch(error => {
    console.log(error.message)
  })