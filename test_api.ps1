# Script de prueba para generar trazas en Axiom
Write-Host "Testing API Vise with OpenTelemetry -> Axiom" -ForegroundColor Cyan
Write-Host ""

$base_url = "http://127.0.0.1:8000"

# Test 1: Access docs
Write-Host "1. Accessing /docs..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "$base_url/docs" -ErrorAction Stop -UseBasicParsing
    Write-Host "   OK Status: $($response.StatusCode)" -ForegroundColor Green
}
catch {
    Write-Host "   Error: $_" -ForegroundColor Red
}

Start-Sleep -Seconds 2

# Test 2: Access redoc
Write-Host "2. Accessing /redoc..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "$base_url/redoc" -ErrorAction Stop -UseBasicParsing
    Write-Host "   OK Status: $($response.StatusCode)" -ForegroundColor Green
}
catch {
    Write-Host "   Error: $_" -ForegroundColor Red
}

Start-Sleep -Seconds 2

Write-Host ""
Write-Host "Tests completed - Traces sent to Axiom dataset: devops" -ForegroundColor Green
Write-Host "Check Axiom: https://app.axiom.co/" -ForegroundColor Cyan
