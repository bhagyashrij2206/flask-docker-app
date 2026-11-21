from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home_page():
    response = client().get("/")
    assert response.status_code == 200
    assert b"Hello from Flask in Docker!" in response.data


def test_health_check():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
