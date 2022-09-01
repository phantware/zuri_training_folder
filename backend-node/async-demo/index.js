console.log('Before')
getUser(1, getRepositories)

console.log('After')
// We use named functio to resolve callback hell
function getRepositories(user) {
  getRepositories(user.githubUsername, getCommits)
}
function getCommits(repo) {
  getCommits(repo[0], displayCommits)
}
function displayCommits(commits) {
  console.log('commits', commits)
}

function getUser(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log('Reading a user from a database...')
      resolve({ id: id, githubUsername: 'jamiu' })
    }, 2000)
  })
}

function getRepositories(username) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(['repo 1', 'repo 2', 'repo 3'])
    }, 2000)
  })
}
