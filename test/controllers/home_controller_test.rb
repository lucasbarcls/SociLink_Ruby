require "test_helper"

class HomeControllerTest < ActionDispatch::IntegrationTest
  test "should get cadastro" do
    get home_cadastro_url
    assert_response :success
  end
end
