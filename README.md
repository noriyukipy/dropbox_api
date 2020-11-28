# Dropbox API

This tool allows you upload your file to Dropbox.

## Install

```sh
$ pip install git+https://github.com/noriyukipy/dropbox_api
```

## Preparation

1. Create your app in Dropbox https://www.dropbox.com/developers/apps
   - Choose an API: Scoped access
   - Choose the type of access you need: App folder
   - Name your app: <YOUR_APP_NAME>
1. Move to "Permission" tab and add permission to "files.content.read" and "files.content.write"
1. Return back to "Settings" tab and generate "access token"

You can find the `App/<YOUR_APP_NAME>` direcotry in your Dropbox. All the files uploaded by this program are placed there.

## Usage

Upload your file by `dropbox_api.upload`

```sh
$ python -m dropbox_api.upload <YOUR_ACCESS_TOKEN_HERE> path/to/local/file /dropbox/target/dir
```

You can find your uploaded file in your Dropbox by `/App/<YOUR_APP_NAME>/dropbox/target/dir/file`