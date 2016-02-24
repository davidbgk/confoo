describe('Testing application tags', () => {
  const qSA = document.querySelectorAll.bind(document)
  const qS = document.querySelector.bind(document)

  it('checks the twt-title tag content', () => {
    const title = qS('twt-title > h1')
    expect(title.textContent).to.be('mnmlst twt')
  })

  it('checks the twt-list inner tags once loaded', () => {
    const items = qSA('twt-item')
    expect(items.length).to.be(tweets.data.length)
  })

  it('checks the twt-form username input value', () => {
    const username = qS('twt-form [name="username"]')
    expect(username.value).to.be('davidbgk')
  })

  it('checks the usernamize function', () => {
    if (!qS('twt-item')) return
    const usernamize = qS('twt-item')._tag.usernamize
    expect(usernamize('hello @confooca'))
      .to.be('hello <a href="#confooca">@confooca</a>')
  })

})
