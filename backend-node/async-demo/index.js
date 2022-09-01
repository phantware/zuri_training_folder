console.log('Before')
getUser(1, getRepositories)

console.log('After')
// We use named functio to resolve callback hell
function getRepositories(user) {
  getRepositories(user.githubUsername, getCommits)
}
function getCommits(repo) {
  getCommits(repo, displayCommits)
}
function displayCommits(commits) {
  console.log('commits', commits)
}

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
