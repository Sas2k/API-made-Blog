# API-Blog

A blog made with FastAPI that can create blog posts with api requests.

## Adding a post

Before adding a post send a get request to.

`/posts`

to check how many posts are there.

Then create your post and put the body and send a request to

`/posts/post`.

## API Reference

#### Hello World

```http
GET /
```

#### Get all posts

```http
GET /posts
```

#### Get item

```http
GET /posts/get/${id}
```

| Parameter | Type       | Description                       |
| :-------- | :--------- | :-------------------------------- |
| `id`      | `interger` | **Required**. Id of item to fetch |

#### Post Item

```http
POST /posts/post
```

##### body 

| Parameter | Type       | Description                       |
| :-------- | :--------- | :-------------------------------- | 
| `title`   | `string`   | **Required** The title            |
| `body`    | `string`   | **Required** The body             |
| `UserID`  | `interger` | **Required** The User ID          |
| `PostID`  | `interger` | **Required** The Post ID          |

#### HTML Post

```http
GET /blog/${id}
```
| Parameter | Type       | Description                       |
| :-------- | :--------- | :-------------------------------- |
| `id`      | `interger` | **Required**. Id of item to fetch |

you can actually visit this page.
