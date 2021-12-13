import albumentations as A

PIP_CONFIGS = {
    'DEFAULT_TF': [
            A.Sharpen(p=1.0)
        ],
    
    'PIXEL_TF': [
        A.AdvancedBlur(),
        A.Blur(),
        A.CLAHE(p=1.0), # suggested
        A.ChannelDropout(),
        A.ChannelShuffle(),
        A.ColorJitter(),
        A.Downscale(),
        A.Emboss(),
        A.Equalize(),
        #A.FDA(),
        A.FancyPCA(),
        A.FromFloat(), # white 10
        A.GaussNoise(),
        A.GaussianBlur(),
        A.GlassBlur(),
        #A.HistogramMatching(),
        A.HueSaturationValue(),
        A.ISONoise(),
        A.ImageCompression(),
        A.InvertImg(), # color negative 17
        A.MedianBlur(),
        A.MotionBlur(),
        A.MultiplicativeNoise(), # suggested
        A.Normalize(), # blacked 21
        #A.PixelDistributionAdaptation(),
        A.Posterize(),
        A.RGBShift(),
        A.RandomBrightnessContrast(),
        A.RandomFog(),
        A.RandomGamma(),
        A.RandomRain(),
        A.RandomShadow(),
        A.RandomSnow(),
        A.RandomSunFlare(),
        A.RandomToneCurve(),
        A.RingingOvershoot(),
        A.Sharpen(p=1.0), # suggested
        A.Solarize(),
        A.Superpixels(), # 뭉개짐 35
        #A.TemplateTransform(),
        A.ToFloat(), # blacked 36
        A.ToGray(),
        A.ToSepia(),
        A.UnsharpMask()
        ], # 40

    'spacial_tf': [
        A.Affine(),
        #A.CenterCrop(),
        #A.CropAndPad(),
        #A.CropNonEmptyMaskIfExists(),
        A.HorizontalFlip(),
        A.Lambda(),
        A.LongestMaxSize(),
        A.PadIfNeeded(),
        A.Perspective(),
        A.PiecewiseAffine(),
        #A.RandomCrop(),
        #A.RandomCropNearBBox(),
        #A.RandomResizedCrop(),
        A.RandomRotate90(),
        A.RandomScale(),
        #A.RandomSizedCrop(),
        #A.Resize(),
        A.Rotate(),
        A.SafeRotate(),
        A.ShiftScaleRotate(),
        A.SmallestMaxSize(),
        A.Transpose(),
        A.VerticalFlip()
    ] # 15
}