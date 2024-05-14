var client = new Parse.LiveQueryClient({
    applicationId: 'mKBbm0wXkcNolPQw1wkssxgCttS0gnjeThdCdXEt',
    serverURL: 'wss://' + 'https://giappi-k12.b4a.app/', // Example: 'wss://livequerytutorial.back4app.io'
    javascriptKey: 'pvJCEZwSF3VVomRSt96w3hFwWNcYz32QiUBRrBKf'
});
client.open();