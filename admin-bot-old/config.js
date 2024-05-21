const sleep = time => new Promise(resolve => setTimeout(resolve, time))

const challenges = new Map([
  ['cooltextgenerator', {
    name: 'Cool Text Generator',
    timeout: 10000,
    handler: async (url, ctx) => {
      const page = await ctx.newPage()
      await page.setCookie({ name: 'flag', value: 'mctf{b3w4r3_0f_x55_7cd6d4d8}', url })
      await page.goto(url, { timeout: 3000, waitUntil: 'domcontentloaded' })
      await sleep(5000)
    },
    urlRegex: /^https:\/\/amateurs-ctf-2024-sculpture-challenge\.pages\.dev/,
  }]
])

module.exports = {
  challenges
}
