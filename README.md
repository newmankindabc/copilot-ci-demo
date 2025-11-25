# FastAPI 示例服务

该项目使用 Python 3 + FastAPI 实现了一个最小可运行的 HTTP 服务，包含健康检查与求和两个接口。

## 环境准备

1. 建议使用 Python 3.11（或兼容版本）。
2. 安装依赖：

   ```bash
   python -m pip install fastapi uvicorn
   ```

## 启动服务

```bash
python main.py
```

默认会使用 Uvicorn 启动服务，监听 `http://0.0.0.0:8000`，并启用热重载。

## 可用接口

| 方法 | 路径        | 描述                        | 示例                                      |
|------|-------------|-----------------------------|-------------------------------------------|
| GET  | `/health`   | 健康检查，返回服务状态      | `curl http://localhost:8000/health`       |
| GET  | `/sum`      | 计算 `x` 与 `y` 的和        | `curl "http://localhost:8000/sum?x=1&y=2"` |

### `/health`

**响应示例**

```json
{"status": "ok"}
```

### `/sum`

查询参数 `x`、`y` 均为必填，并支持浮点数。缺失参数时会返回 400 错误。

**响应示例**

```json
{"result": 3}
```

## 开发说明

- 代码主入口：`main.py`
- FastAPI 文档与测试页面可访问：
  - Swagger UI: `http://localhost:8000/docs`
  - ReDoc: `http://localhost:8000/redoc`

欢迎根据需要扩展更多业务逻辑。

