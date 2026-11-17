Add-Type -AssemblyName System.Drawing

$iconDirectory = Join-Path $PSScriptRoot '..\icons'
New-Item -ItemType Directory -Force -Path $iconDirectory | Out-Null

foreach ($size in @(180, 192, 512)) {
    $bitmap = [System.Drawing.Bitmap]::new($size, $size)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $graphics.ScaleTransform($size / 512.0, $size / 512.0)
    $graphics.Clear([System.Drawing.Color]::FromArgb(255, 255, 223, 132))

    $ink = [System.Drawing.Color]::FromArgb(255, 38, 51, 66)
    $blue = [System.Drawing.Color]::FromArgb(255, 76, 115, 217)
    $pageLine = [System.Drawing.Color]::FromArgb(255, 184, 200, 245)
    $sunBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::FromArgb(255, 255, 223, 132))
    $blueBrush = [System.Drawing.SolidBrush]::new($blue)
    $whiteBrush = [System.Drawing.SolidBrush]::new([System.Drawing.Color]::White)
    $inkPen = [System.Drawing.Pen]::new($ink, 12)
    $foldPen = [System.Drawing.Pen]::new($ink, 10)
    $detailPen = [System.Drawing.Pen]::new($pageLine, 9)
    foreach ($pen in @($inkPen, $foldPen, $detailPen)) {
        $pen.StartCap = [System.Drawing.Drawing2D.LineCap]::Round
        $pen.EndCap = [System.Drawing.Drawing2D.LineCap]::Round
    }

    $graphics.FillEllipse($blueBrush, 52, 62, 408, 408)
    $graphics.FillEllipse($sunBrush, 220, 106, 72, 72)

    $leftPage = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $leftPage.AddBezier(120, 202, 167, 184, 216, 194, 256, 222)
    $leftPage.AddLine(256, 222, 256, 365)
    $leftPage.AddBezier(256, 365, 214, 338, 164, 333, 120, 351)
    $leftPage.CloseFigure()
    $graphics.FillPath($whiteBrush, $leftPage)
    $graphics.DrawPath($inkPen, $leftPage)

    $rightPage = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $rightPage.AddBezier(392, 202, 345, 184, 296, 194, 256, 222)
    $rightPage.AddLine(256, 222, 256, 365)
    $rightPage.AddBezier(256, 365, 298, 338, 348, 333, 392, 351)
    $rightPage.CloseFigure()
    $graphics.FillPath($whiteBrush, $rightPage)
    $graphics.DrawPath($inkPen, $rightPage)

    $graphics.DrawLine($foldPen, 256, 226, 256, 365)
    $graphics.DrawLine($detailPen, 145, 250, 227, 266)
    $graphics.DrawLine($detailPen, 145, 281, 227, 297)
    $graphics.DrawLine($detailPen, 367, 250, 285, 266)
    $graphics.DrawLine($detailPen, 367, 281, 285, 297)
    $graphics.DrawBezier($inkPen, 108, 386, 159, 360, 207, 369, 256, 397)
    $graphics.DrawBezier($inkPen, 256, 397, 305, 369, 353, 360, 404, 386)

    $fileName = if ($size -eq 180) { 'icon-180.png' } elseif ($size -eq 192) { 'icon-192.png' } else { 'icon-512.png' }
    $bitmap.Save((Join-Path $iconDirectory $fileName), [System.Drawing.Imaging.ImageFormat]::Png)

    $leftPage.Dispose()
    $rightPage.Dispose()
    $sunBrush.Dispose()
    $blueBrush.Dispose()
    $whiteBrush.Dispose()
    $inkPen.Dispose()
    $foldPen.Dispose()
    $detailPen.Dispose()
    $graphics.Dispose()
    $bitmap.Dispose()
}
