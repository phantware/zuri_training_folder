console.log('Before')
getUser(1, function (user) {
  getRepositories(user.githubUsername, function (repo) {
    getCommits(repo, (commits) => {
      console.log('commits', commits)
    })
  })
})

console.log('After')

function getUser(id, callback) {
  setTimeout(() => {
    console.log('Reading a user from a database...')
    callback({ id: id, githubUsername: 'jamiu' })
  }, 2000)
}

function getRepositories(username, callback) {
  setTimeout(() => {
    callback(['repo 1', 'repo 2', 'repo 3'])
  }, 2000)
}
