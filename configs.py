import albumentations as A


PIP_CONFIGS = {
    'DEFAULT_TF': [
            A.Sharpen(p=1.0)
        ],
    
    'PIXEL_TF': [
        A.AdvancedBlur(p=1.0),
        #A.Blur(p=1.0),
        A.CLAHE(p=1.0), # suggested
        #A.ChannelDropout(p=1.0),
        A.ChannelShuffle(p=1.0),
        A.ColorJitter(p=1.0),
        A.Downscale(p=1.0),
        A.Emboss(p=1.0),
        A.Equalize(p=1.0),
        #A.FDA(),
        #A.FancyPCA(p=1.0),
        #A.FromFloat(), # white 10
        A.GaussNoise(p=1.0),
        #A.GaussianBlur(p=1.0),
        A.GlassBlur(p=1.0),
        #A.HistogramMatching(),
        A.HueSaturationValue(p=1.0),
        A.ISONoise(p=1.0),
        #A.ImageCompression(p=1.0),
        #A.InvertImg(p=1.0), # color negative 17
        #A.MedianBlur(p=1.0),
        #A.MotionBlur(p=1.0),
        A.MultiplicativeNoise(p=1.0), # suggested
        #A.Normalize(), # blacked 21
        #A.PixelDistributionAdaptation(),
        #A.Posterize(p=1.0),
        #A.RGBShift(p=1.0),
        A.RandomBrightnessContrast(p=1.0),
        #A.RandomFog(p=1.0),
        #A.RandomGamma(p=1.0),
        A.RandomRain(p=1.0),
        A.RandomShadow(p=1.0),
        #A.RandomSnow(p=1.0),
        #A.RandomSunFlare(p=1.0),
        A.RandomToneCurve(p=1.0),
        A.RingingOvershoot(p=1.0),
        #A.Sharpen(p=1.0), # suggested
        #A.Solarize(p=1.0),
        #A.Superpixels(), # 뭉개짐 35
        #A.TemplateTransform(),
        #A.ToFloat(p=1.0), # blacked 36
        A.ToGray(p=1.0),
        #A.ToSepia(p=1.0),
        A.UnsharpMask(p=1.0)
        ], # 40

    'SPACIAL_TF': [
        A.Affine(p=1.0),
        #A.CenterCrop(),
        #A.CropAndPad(),
        #A.CropNonEmptyMaskIfExists(),
        A.HorizontalFlip(p=1.0),
        #A.Lambda(p=1.0),
        #A.LongestMaxSize(p=1.0),
        A.PadIfNeeded(p=1.0),
        A.Perspective(p=1.0),
        A.PiecewiseAffine(p=1.0),
        #A.RandomCrop(),
        #A.RandomCropNearBBox(),
        #A.RandomResizedCrop(),
        A.RandomRotate90(p=1.0),
        A.RandomScale(p=1.0),
        #A.RandomSizedCrop(),
        #A.Resize(),
        A.Rotate(p=1.0),
        #A.SafeRotate(p=1.0),
        #A.ShiftScaleRotate(p=1.0),
        #A.SmallestMaxSize(p=1.0),
        A.Transpose(p=1.0),
        A.VerticalFlip(p=1.0)
    ] # 15
}